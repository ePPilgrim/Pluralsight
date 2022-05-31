from .icarfactory import ICarFactory
from autos.cars import ChevyVolt

class ChevyFactory(ICarFactory):

    def create_auto(self):
        self.chevy = chevy = ChevyVolt()
        chevy.name = 'Chevy Volt'
        return chevy