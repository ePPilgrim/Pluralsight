from .icarfactory import ICarFactory
from autos.cars import NullCar

class NullCarFactory(ICarFactory):

    def create_auto(self):
        self.nullcar = nullcar = NullCar()
        return nullcar