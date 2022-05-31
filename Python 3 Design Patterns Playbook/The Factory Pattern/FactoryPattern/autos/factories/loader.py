from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .icarfactory import ICarFactory

def load_factory(factory_name):
    try:
        factory_module = import_module('.' + factory_name, 'autos.factories')
    except ImportError:
        factory_module = import_module('.nullfactory', 'autos.factories')

    classes = getmembers(factory_module, lambda m: isclass(m) and not isabstract(m))

    for _, _class in classes:
        if issubclass(_class, ICarFactory):
            return _class()