# 1. Даны 4 числа типа int. Сравнить их и вывести наименьшее на консоль.
# 2. Вывести на консоль количество максимальных чисел среди этих четырех.

def find_min(x,y):
    if x < y:
        return x
    else:
        return y

def find_max(x,y):
    if x > y:
        return x
    else:
        return y

def print_min(x,y):
    if x < y:
        mymin = x
    else:
        mymin = y
    print("mymin =", mymin)

def find_and_print_max_count():
    max_local = find_max(find_max(a, b), find_max(c, d))
    count_max = 0
    if max_local == a:
        count_max += 1
    if max_local == b:
        count_max += 1
    if max_local == c:
        count_max += 1
    if max_local == d:
        count_max += 1
    print("max =", max_local)
    print("count max =", count_max)


a = 2
b = 1
c = 3
d = 3

print_min(10,20)

min_local = find_min(find_min(a,b),find_min(c,d))

print("min =",min_local)

find_and_print_max_count()