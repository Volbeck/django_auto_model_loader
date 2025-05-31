import inflection
from django.utils.deprecation import MiddlewareMixin
from django.apps import apps
from django.utils.functional import SimpleLazyObject

from .aliases import get_model_by_alias


def _get_module_name_from_request(self, request):
    match = getattr(request, 'resolver_match', None)
    if not match:
        return None

    view_func = match.func
    view_class = getattr(view_func, 'view_class', None)

    module_path = view_class.__module__ if view_class else view_func.__module__
    app_name = module_path.split('.')[0]

    return app_name

def _get_model_from_apps(alias: str):
    model_name = inflection.camelize(alias, uppercase_first_letter=True)
    for app_config in apps.get_app_configs():
        try:
            return app_config.get_model(model_name)
        except LookupError:
            continue
    return None


class AutoModelLoaderMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        module_name = _get_module_name_from_request(self, request)
        if not module_name:
            return None

        for key in filter(lambda k: k.endswith('_pk'), view_kwargs.keys()):
            alias = key[:-3]
            pk = view_kwargs[key]
            model_class = _get_model_from_apps(alias) or get_model_by_alias(module_name, alias)
            if not model_class:
                continue

            setattr(request, alias, SimpleLazyObject(lambda mc=model_class, pk_=pk: mc.objects.filter(pk=pk_).first()) )

        return None