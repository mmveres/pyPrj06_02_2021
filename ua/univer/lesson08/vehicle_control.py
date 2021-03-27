# 1. вывести на екран механизм с наибольшей ценой
# 2. получить механизм с наименьшей ценой
# 3. получить механизм с ценой меньше 10000
#    после 2000 года
# 4. получить масив механизмов год выпуска
#    с 2000 по 2010
# 5. получить масив механизмов не старше 5 лет
#    с средней ценой(+- 20%) и
#    скоростью в диапазоне от 100 до 200
# 6. в масиве механизмов получить количество Car
#    и Plane
# 7. получить из масива механизмов Car с
#    наименьшей ценой
# 8. получить из масива механизмов масив Ship год
#    выпуска с 2000 по 2010
# 9. добавить классы Amfibia, BatMobile
# 10. создать класи
# MoveAble{ int move()},
# SwimAble{ int swim()},
# FlyAble { int fly()}
# и создать три массива
# 11. в каждом масиве подсчитать
# среднюю цену,
# максимальную скорость,
# минимальный год выпуска,
# даны GPS-координаты кто ближе к указаной точке.
from ua.univer.lesson08.vehicles import *


class VehicleControl:
    def __init__(self, vehicle_list):
        self.vehicle_list = vehicle_list

    def print_max_price_vehicle(self):
        max_price_vehicle = self.vehicle_list[0]
        for vehicle in self.vehicle_list:
            if vehicle.price > max_price_vehicle.price:
                max_price_vehicle = vehicle
        print(max_price_vehicle)

    def get_list_between_year(self,year_begin, year_end):
        vehicles_between_year = []
        for vehicle in self.vehicle_list:
            if year_begin<vehicle.year<year_end:
                vehicles_between_year.append(vehicle)
        return vehicles_between_year

    def print_count_Car_Plane(self):
        count_car = 0
        count_plane = 0
        count_swim = 0
        for vehicle in self.vehicle_list:
            if isinstance(vehicle,Car):
                count_car+=1
            if isinstance(vehicle,Plane):
                count_plane+=1
            if isinstance(vehicle,SwimAble):
                count_swim+=1
        print("count_car =",count_car)
        print("count_plane =",count_plane)
        print("count_swim =",count_swim)

