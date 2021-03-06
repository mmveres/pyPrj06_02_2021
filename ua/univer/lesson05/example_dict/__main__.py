if __name__ == '__main__':
    users = {
        "+11111111": "Tom",
        "+33333333": "Bob",
        "+55555555": "Alice"
    }
    for key, values in users.items():
        print(key, values)
    print(users)