from .icar import ICar 

class ChevyVolt(ICar):
    
    def start(self):
        print('Chevrolet Volt running with shocking power!')
    
    def stop(self):
        print('Chevrolet Volt shutting down.')