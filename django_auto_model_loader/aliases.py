_model_alias_registry = {}
_model_reverse_registry = {}

def register_model_alias(model, *aliases):
    module_name = model.__module__.split('.')[0]
    for alias in aliases:
        _model_alias_registry[(module_name, alias)] = model
        _model_reverse_registry.setdefault(model, set()).add((module_name, alias))

def get_model_by_alias(module_name, alias):
    return _model_alias_registry.get((module_name, alias))

def get_aliases_for_model(model):
    return _model_reverse_registry.get(model, set())


