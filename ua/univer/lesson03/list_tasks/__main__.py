from ua.univer.lesson03.list_tasks.tasks_list import *
if __name__ == '__main__':
    while(True):
        print("""1.создайте массив, содержащий 10 первых нечетных чисел.
        Выведете элементы массива на консоль в одну строку, разделяя запятой""")
        print("""2.ввести 10 целых значений с консоли и разместить в
             2 масива четные и нечетные""" )
        print("0. Exit")

        answer = input("enter choice")
        if answer == "0":
            break
        elif answer == "1":
            print(task01_get10odd())
        elif answer == "2":
           list_even, list_odd = get_even_odd_list_from_console()
           print(list_even)
           print(list_odd)
