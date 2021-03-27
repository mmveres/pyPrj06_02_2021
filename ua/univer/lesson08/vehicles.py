# Создать абстрактный класс Vehicle.
# На его основе реализовать классы Plane, Саг и Ship.
# Классы должны иметь возможность задавать и получать координаты,
# параметры средств передвижения (цена, скорость, год выпуска).
# Для самолета должна быть определена высота,
# для самолета и корабля — количество пассажиров.
# Для корабля — порт приписки.
# Написать программу, создающую список объектов этих классов
# в динамической памяти.
# Программа должна содержать меню,
# позволяющее осуществить проверку всех методов классов.
import abc
from abc import ABC

from ua.univer.lesson08.coordinate import Point
from ua.univer.lesson08.passenger import Passenger
from ua.univer.lesson08.vehicle_ables import SwimAble


class Vehicle(metaclass=abc.ABCMeta):
    def __init__(self, point: Point, price: float, speed: float, year: int):
        self.point = point
        self.price = price
        self.speed = speed
        self.year = year

    def __str__(self) -> str:
        return f"{self.point}, {self.price},{self.speed},{self.year}"

    @abc.abstractmethod
    def show_image(self):
        pass


class Plane(Vehicle,metaclass=abc.ABCMeta):
    def __init__(self, point, price, speed, year, height):
        super().__init__(point, price, speed, year)
        self.height = height

    def __str__(self) -> str:
        return f"{super().__str__()},{self.height}"

    def __repr__(self) -> str:
        return f"\nPlane: {self.__str__()}"

    def fly(self):
        return self.speed

    def show_image(self):
        print("Plane")

class PlanePassenger(Plane,Passenger):
    def __init__(self, point, price, speed, year, height, count_pass):
        super().__init__(point, price, speed, year, height)
        Passenger.__init__(self,count_pass)

    def __str__(self) -> str:
        return f"{super().__str__()},{self.height},{self.count_pass}"

    def __repr__(self) -> str:
        return f"\nPlanePassenger: {self.__str__()}"

class PlaneCargo(Plane):
    def __init__(self, point, price, speed, year, height, cargo_weight):
        super().__init__(point, price, speed, year, height)
        self.cargo_weight = cargo_weight

    def __str__(self) -> str:
        return f"{super().__str__()},{self.height},{self.cargo_weight}"

    def __repr__(self) -> str:
        return f"\nPlaneCargo: {self.__str__()}"

    def show_image(self):
        print("PlaneCargo")

class Ship(Vehicle,Passenger, SwimAble):
    def __init__(self, point, price, speed, year, port, count_pass):
        Vehicle.__init__(self,point, price, speed, year)
        Passenger.__init__(self,count_pass)
        self.port = port

    def __str__(self) -> str:
        return f"{super().__str__()},{self.port},{self.count_pass}"

    def __repr__(self) -> str:
        return f"\nShip: {self.__str__()}"

    def show_image(self):
        print("Ship")

    def swim(self):
        return self.speed


class Car(Vehicle):
    def __init__(self, point, price, speed, year):
        super().__init__(point, price, speed, year)

    def __repr__(self) -> str:
        return f"\nCar: {self.__str__()}"

    def show_image(self):
        print("Car")

    def move(self):
        return self.speed

class Amfibian(Car, SwimAble):

    def __init__(self, point, price, speed, year):
        super().__init__(point, price, speed, year)

    def swim(self):
        return self.speed/2

