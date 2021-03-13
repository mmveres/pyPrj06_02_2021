def input_float_from_console():
    while True:
        try:
            value = float(input("Enter float value"))
            return value
        except:
            print("Error not float")


def input_int_from_console():
    while True:
        try:
            value = int(input("Enter int value"))
            return value
        except:
            print("Error not int")


class Helper:
    pass
