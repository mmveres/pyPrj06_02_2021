import random


def fill_data():
    while True:
        try:
            min_number_of_range = int(input('Please enter min number of range: '))
            max_number_of_range = int(input('Please enter max number of range: '))
            num_of_num = int(input('Please enter number of numbers: '))
            break;
        except ValueError:
            print('Data is not correct. Try again', ValueError)
    return min_number_of_range, max_number_of_range, num_of_num


def write_random_numbers(filename, min_number_of_range, max_number_of_range, num_of_num):
    try:
        edit_file = open(filename, 'a')
        for num in range(num_of_num):
            edit_file.write((str(random.randrange(min_number_of_range, max_number_of_range))) + '\n')
    except IOError:
        print('Data is not correct. Try again', IOError)
    finally:
        edit_file.close()


def arithmetic_mean(filename):
    try:
        read_file = open(filename, 'r')
        list_from_file = read_file.readlines()
    except IOError:
        print('Data is not correct. Try again', IOError)
        return
    finally:
        read_file.close()
    i = 0
    sum_numbers_of_list = 0
    while i < len(list_from_file):
        list_from_file[i] = list_from_file[i].strip('\n')
        sum_numbers_of_list += int(list_from_file[i])
        i += 1
    print('Number in file ', filename, '- ', list_from_file)
    print("Summ of numbers = ", sum_numbers_of_list)
    print("Number of numbers = ", i)
    print("Arithmetic mean = ", format((sum_numbers_of_list / i), '.2f'))

if __name__ == '__main__':
    print("Hello from mylib")
    fill_data()