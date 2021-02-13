hour = int(input("time hour = "))
age = int(input("age = "))
if hour<22:
    if age>18:
        print("you can buy alcohol")
    else:
        print("you can buy pepsi")
else:
    print("market close")