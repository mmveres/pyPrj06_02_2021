import task_if_lib

while True:
    print(" 1. Даны 4 числа типа int. Сравнить их и вывести наименьшее на консоль.")
    print(" 2. Вывести на консоль количество максимальных чисел среди этих четырех.")
    print(""" 3. Даны 5 чисел (тип int). Вывести вначале наименьшее,
            а затем наибольшее из данных чисел.""")
    print(""" 4. Даны имена 2х человек (тип string). Если имена равны,
 	        то вывести сообщение о том, что люди являются тезками.""")
    print(""" 5. Дано число месяца (тип int). Необходимо определить время года
 	        (зима, весна, лето, осень) и вывести на консоль.""")
    print("0. Exit")
    answer = int(input("enter choice"))
    if answer == 0:
        break;
    elif answer == 1:
        a = 2
        b = 1
        c = 3
        d = 3
        min_local = task_if_lib.get_min(task_if_lib.get_min(a, b), task_if_lib.get_min(c, d))
        print("min =",min_local)
    elif answer == 2:
        task_if_lib.find_and_print_max_count()
    elif answer in range(3,6):
        print("Not yet")
    else:
        print("Wrong choice, try again.")






