from .icar import ICar

class FordFusion(ICar):
    
    def start(self):
        print('FordFusion running with shocking power!')
    
    def stop(self):
        print('FordFusion shutting down.')