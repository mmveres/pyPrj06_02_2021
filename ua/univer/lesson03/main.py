def list_test():
    arr = [1, 23, 4, 5, 6, 7]
    for value in arr:
        value += 1
        print(value)
    for i in range(0, len(arr), 1):
        arr[i] += 2
        print("arr[", i, "] =", arr[i])
    arr.append(10)
    arr[2] = 3333
    arr.insert(4, 8888)
    for i in range(len(arr)):
        print("arr[", i, "] =", arr[i])
    print(arr)
    for value in arr:
        print(value)


def get_int_from_console():
    while (True):
        try:
            value = int(input("Enter value"))
            return value
        except:
            print("Error value not int")


def get_mark_from_int():
    while (True):
        try:
            value = get_int_from_console()
            if 3 > value or value >= 12:
                raise Exception("value not in range (3 , 12)")
            return value
        except Exception as e:
            print("Error value not mark", e)


if __name__ == '__main__':
    arr_marks = []
    while (True):
        mark = get_mark_from_int()
        arr_marks.append(mark)
        answer = input("exit[y]")
        if answer.lower() == "y":
            break

    print(arr_marks)
