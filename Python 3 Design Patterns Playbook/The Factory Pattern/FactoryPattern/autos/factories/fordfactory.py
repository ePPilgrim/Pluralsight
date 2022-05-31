from .icarfactory import ICarFactory
from autos.cars import FordFusion

class FordFactory(ICarFactory):

    def create_auto(self):
        self.ford = ford = FordFusion()
        ford.name = 'Ford Fusion'
        return ford