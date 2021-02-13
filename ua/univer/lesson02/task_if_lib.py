# 1. Даны 4 числа типа int. Сравнить их и вывести наименьшее на консоль.
# 2. Вывести на консоль количество максимальных чисел среди этих четырех.
# 3. Даны 5 чисел (тип int). Вывести вначале наименьшее,
#    а затем наибольшее из данных чисел.
# 4. Даны имена 2х человек (тип string). Если имена равны,
# 	то вывести сообщение о том, что люди являются тезками.
# 5. Дано число месяца (тип int). Необходимо определить время года
# 	(зима, весна, лето, осень) и вывести на консоль.

def task03_print_5_min_max(a,b,c,d,e):
    pass

def task04_compare_2_human(name1, name2):
    pass

def task05_print_season(month_number):
    pass

def get_min(x, y):
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

def find_and_print_max_count(a,b,c,d):
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