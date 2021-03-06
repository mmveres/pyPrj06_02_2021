import codecs
import csv
import json


def print_file(filename = "zp-lupen-2019.csv"):
    with open(filename, "r", encoding="1251") as file:
        for line in file:
            print(line)


def print_max_oklad_kmda(kmda_dict_users):
    max_oklad = 0
    max_oklad_name = ""
    for kmda_user in kmda_dict_users:
        if max_oklad < float(kmda_dict_users[kmda_user]['Оплата по окладу'].replace(',', '.')):
            max_oklad = float(kmda_dict_users[kmda_user]['Оплата по окладу'].replace(',', '.'))
            max_oklad_name = kmda_dict_users[kmda_user]['Працівник']
            print(kmda_user)
            print(kmda_dict_users[kmda_user]['Оплата по окладу'])
    print(max_oklad_name, max_oklad)


def save_with_encode(kmda_dict_users):
    with open("kmda.json", "w", encoding='utf-8') as file:
        file.write(json.dumps(kmda_dict_users))


def get_dict_kmda_from_csv(filename):
    kmda_dict_users = {}
    with open(filename, "r", encoding="1251") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            kmda_dict = dict(row)
            kmda_dict_users[kmda_dict["Працівник"]] = kmda_dict
    return kmda_dict_users

if __name__ == '__main__':
    filename = "zp-lupen-2019.csv"
    kmda_dict_users = get_dict_kmda_from_csv(filename)
    print(kmda_dict_users)
    print_max_oklad_kmda(kmda_dict_users)

#    save_with_encode(kmda_dict_users)