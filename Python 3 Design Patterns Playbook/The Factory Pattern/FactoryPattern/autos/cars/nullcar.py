from .icar import ICar

class NullCar(ICar):

    def start(self):
        print(f'Unknown car.')
    
    def stop(self):
        print('Car shutting down.')