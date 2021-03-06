import csv
if __name__ == '__main__':

    FILENAME = "users.csv"

    users = [
        ["Tom", 28],
        ["Alice", 23],
        ["Bob", 34]
    ]

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(users)


    with open(FILENAME, "a", newline="") as file:
        user = ["Sam", 31]
        writer = csv.writer(file, delimiter=';')
        writer.writerow(user)

    with open(FILENAME, "r", newline="") as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row[0], " - ", row[1])