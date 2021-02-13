def print_10_positive():
    i = 0
    while i < 10:
        value = int(input("enter positive value"))
        if value >= 0:
            i += 1
            print("count=", i, "value =", value)
        else:
            print("not positive")

def pow(x,n):
    value = 1
    for i in range(n):
        value *= x
    return value


def calc_power_value_from_console():
    x = int(input("enter value x"))
    n = int(input("power n"))
    print("x =", x, " in power", n, "=", pow(x, n))