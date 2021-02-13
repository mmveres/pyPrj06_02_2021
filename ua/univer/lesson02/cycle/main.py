import tasks_cycle, constant

constant.PI = 8

while True:
    print("------------MENU----------")
    print("1. print 10 positive value")
    print("2. calc power from console")
    print("3. calc power")
    print("0. Exit")
    print("--------------------------")
    answer = int(input("enter choice"))
    if answer == 0:
        break;
    elif answer == 1:
        tasks_cycle.print_10_positive()
    elif answer == 2:
        tasks_cycle.calc_power_value_from_console()
    elif answer == 3:
        print(tasks_cycle.pow(3,2))
    else:
        print("Wrong choice, try again.")





