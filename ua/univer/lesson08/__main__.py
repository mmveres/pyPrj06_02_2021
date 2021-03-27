from ua.univer.lesson08.vehicles import *

if __name__ == '__main__':
    vehicle_list = [PlanePassenger(Point(1, 2), 10000, 200, 1990, 20, 15),
                    PlaneCargo(Point(2, 3), 10000, 200, 1990, 20, 2500),
                    Ship(Point(3, 4), 20000, 200, 1990, "Odessa", 150),
                    Car(Point(4, 5), 5000, 200, 1990)
                    ]
    print(vehicle_list)
    for vehicle in vehicle_list:
        vehicle.show_image()
