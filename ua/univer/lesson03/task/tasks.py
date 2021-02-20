import numpy as np


def main():
    np.set_printoptions(threshold=np.inf)
    np.random.seed(444)
    exec_first()
    exec_second()

def exec_first():
    x = np.random.randint(20, size=100)
    print(x)


def exec_second():
    second_array = []
    while (True):
        try:
            value = int(input("Enter number "))
        except:
            print("Not a number")
        second_array.append(value)
        key = input("exit (y/n): ")
        if key.lower() == "y":
            break
    second_arraynp = np.array(second_array)
    second_arraynpodd = second_arraynp[second_arraynp % 2 == 1]
    second_arraynpeven = second_arraynp[second_arraynp % 2 == 0]
    print(second_arraynpodd)
    print(second_arraynpeven)