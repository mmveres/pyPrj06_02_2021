# 1. Даны 4 числа типа int. Сравнить их и вывести наименьшее на консоль.
# 2. Вывести на консоль количество максимальных чисел среди этих четырех.

def find_min(x,y):
    if x < y:
        return x
    else:
        return y

a = 2
b = 1
c = 3
d = 3

min_local1 = find_min(a,b)
min_local2 = find_min(c,d)
min_local = find_min(min_local1,min_local2)

print(min_local)