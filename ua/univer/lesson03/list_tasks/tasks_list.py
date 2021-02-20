# 1.создайте массив, содержащий 10 первых нечетных чисел.
# Выведете элементы массива на консоль в одну строку, разделяя запятой
# 2.ввести 10 целых значений с консоли и разместить в
# 2 масива четные и нечетные
# 3.подсчитать сколько четные и нечетные
# 4.сумма елементов в каждом масиве и среднее арифметическое
# 5.поменять четные позиции в первом масиве на значения
# нечетных позиций из 2 массива
# 6.Дан массив размерности N,  найти наименьший элемент массива
# и вывести на консоль (если наименьших элементов несколько —
# вывести их индексы).
# 7.Поменять наибольший и наименьший элементы массива местами.
# Пример: дан массив {4, -5, 0, 6, 8}.
# После замены будет выглядеть {4, 8, 0, 6, -5}.

def task01_get10odd():
    mylist = []
    for x in range(1, 20, 2):
        mylist.append(x)
    return mylist


def task01_v1_get10odd():
    return [x for x in range(1, 20, 2)]


def task01_v2_get10odd():
    mylist = []
    count = 0
    value = 0
    while count < 10:
        if value % 2 == 1:
            mylist.append(value)
        value += 1
    return mylist


def task01_v3_get10odd():
    return [x for x in range(20) if x % 2 == 1]


def get_even_odd_list_from_console():
    list_odd = []
    list_even = []
    for i in range(10):
        value = int(input("Enter value"))
        if value % 2 == 0:
            list_even.append(value)
        else:
            list_odd.append(value)
    return list_even, list_odd
