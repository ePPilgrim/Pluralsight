from inspect import getmembers, isclass, isabstract
import autos.cars as cars

class AutoFactory(object):
    autos = {} # Key = car model name, Value = class for the car

    def __init__(self):
        self.load_autos()

    def load_autos(self):
        classes = getmembers(cars, lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, cars.ICar):
                self.autos.update([[name, _type]])
    
    def create_instance(self, carname):
        if carname in self.autos:
            return self.autos[carname]()
        else:
            return cars.NullCar()
