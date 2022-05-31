from .icarfactory import ICarFactory
from autos.cars import JeepSahara

class JeepFactory(ICarFactory):

    def create_auto(self):
        self.jeep = jeep = JeepSahara()
        jeep.name = 'Jeep Sahara'
        return jeep