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

def get_sum(list_elem):
    sum =0
    for x in list_elem:
        sum+=x
    return sum

def get_average(list_elem):
    return get_sum(list_elem)/len(list_elem)

def changev1_min_max_in_list(list_elem):
    mymin =min(list_elem)
    mymax =max(list_elem)
    index_min = list_elem.index(mymin)
    index_max = list_elem.index(mymax)
    list_elem[index_min] = mymax
    list_elem[index_max] =mymin
    print(list_elem)

def change_min_max_in_list(list_elem):
    mymin =min(list_elem)
    mymax =max(list_elem)
    for i in range(len(list_elem)):
        if list_elem[i] == mymax:
            list_elem[i]=mymin
        elif list_elem[i] == mymin:
            list_elem[i]=mymax
    print(list_elem)

if __name__ == '__main__':
    mas =[1,1,5,4,5]
    change_min_max_in_list(mas)