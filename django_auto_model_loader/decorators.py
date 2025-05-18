import inflection
from .aliases import register_model_alias

def model_alias(*aliases):
    def decorator(model_cls):
        all_aliases = set(aliases)
        all_aliases.add(inflection.camelize(model_cls.__name__, False))
        all_aliases.add(inflection.underscore(model_cls.__name__))
        register_model_alias(model_cls, *all_aliases)
        return model_cls
    return decorator