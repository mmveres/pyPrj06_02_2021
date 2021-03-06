# 1. Прочитать из файла info.json данные в dict
# 2. Отобразить количество хобби сотрудника и вывести их на екран
# 3. Сколько детей у сотрудника
# 4. Вывести имя старшего ребенка
# 5. Добавить в dict сотрудника ключ "email": jane@company.com , "phone": 123456
# и сохранить в новый файл info2.json
import json


def task1_get_dict_from_file(filename):
    with open(filename,"r") as file:
        user_str = file.read()
    user_dict = json.loads(user_str)
    return user_dict

def task2_get_count_hobbies_user(user_dict):
    return len(user_dict["hobbies"])

def task3_get_count_child(user_dict):
    return len(user_dict["children"])

def task4_get_oldest_child(user_dict):
    childs = user_dict["children"]
    oldest_year =childs[0]['age']
    oldest_name =childs[0]['firstName']
    for child in childs:
        if oldest_year < child['age']:
            oldest_year=child['age']
            oldest_name=child['firstName']
    return oldest_name

def task5_add_additional_info(user_dict):
    user_dict["email"] = "jane@company.com"
    user_dict["phone"] = 123456

def task6_save_to_file(user_dict, filename):
    with open(filename,"w") as file:
        file.write(json.dumps(user_dict))

if __name__ == '__main__':
    user_dict = task1_get_dict_from_file("info.json")
    print(user_dict)
    task5_add_additional_info(user_dict)
    task6_save_to_file(user_dict, "info2.json")
