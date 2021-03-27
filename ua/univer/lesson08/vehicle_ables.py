import abc


class MoveAble(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def move(self):
        pass

class SwimAble(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def swim(self):
        pass

class FlyAble(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fly(self):
        pass