import abc

class ICarFactory(abc.ABC):

    @abc.abstractmethod
    def create_auto(self):
        pass