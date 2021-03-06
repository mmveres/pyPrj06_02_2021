import csv

if __name__ == '__main__':

    FILENAME = "users.csv"

    users = [
        {"name": "Tom", "age": 28},
        {"name": "Alice", "age": 23},
        {"name": "Bob", "age": 34}
    ]

    with open(FILENAME, "w", newline="") as file:
        columns = ["name", "age"]
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=';')
        writer.writeheader()

        # запись нескольких строк
        writer.writerows(users)

        user = {"name" : "Sam", "age": 41}
        # запись одной строки
        writer.writerow(user)

    with open(FILENAME, "r", newline="") as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            print(row["name"], "-", row["age"])