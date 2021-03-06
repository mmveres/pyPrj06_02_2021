from ua.univer.lesson05.hw.lib.mylib import *


def test_hw():
    filename = input("Enter filename: ")
    min_number_of_range, max_number_of_range, num_of_num = fill_data()
    write_random_numbers(filename, min_number_of_range, max_number_of_range, num_of_num)
    arithmetic_mean(filename)
    write_random_numbers("text.txt", 1, 2, 3)


def swap(x, y):
    return y, x


if __name__ == '__main__':
    x = 2
    y = 3
    z = 4
    x, y = y, x
    x, y = swap(x, y)
    print("x = ", x)
    print("y = ", y)
