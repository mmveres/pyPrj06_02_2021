from ua.univer.lesson08.vehicle_control import VehicleControl
from ua.univer.lesson08.vehicles import *

if __name__ == '__main__':
    vehicle_list = [PlanePassenger(Point(1, 2), 10000, 200, 2000, 20, 15),
                    PlaneCargo(Point(2, 3), 10000, 200, 2005, 20, 2500),
                    Ship(Point(3, 4), 20000, 200, 2020, "Odessa", 150),
                    Car(Point(4, 5), 5000, 200, 2009),
                    Amfibian(Point(4, 5), 15000, 200, 2009),
                    ]
    print(vehicle_list)
    for vehicle in vehicle_list:
        vehicle.show_image()

    vehicle_control = VehicleControl(vehicle_list)
    vehicle_control.print_max_price_vehicle()
    veh_list = vehicle_control.get_list_between_year(2000,2010)
    print(veh_list)
    vehicle_control.print_count_Car_Plane()

    car_list = [Car(Point(4, 5), 5000, 200, 2009),Car(Point(4, 5), 15000, 200, 2009)]
    VehicleControl(car_list).print_max_price_vehicle()
