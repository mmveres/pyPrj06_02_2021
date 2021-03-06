import json


def get_users():
    return {
        "firstName": "Jane",
        "lastName": "Doe",
        "hobbies": ["running", "sky diving", "singing"],
        "age": 35,
        "children": [
            {
                "firstName": "Alice",
                "age": 6
            },
            {
                "firstName": "Bob",
                "age": 8
            }
        ]
    }



if __name__ == '__main__':
    dict_str = json.dumps(get_users())
    print(dict_str)

    dictData = { "ID"       : 210450,
                 "login"    : "admin",
                 "name"     : "John Smith",
                 "password" : "root",
                 "phone"    : 5550505,
                 "email"    : "smith@mail.com",
                 "online"   : True }
    jsonData = json.dumps(dictData)
    with open("data.json", "w") as file:
        file.write(jsonData)

    with open("data.json", "r") as file:
        json_str = file.read()
    json_dict = json.loads(json_str)
    print(json_dict)