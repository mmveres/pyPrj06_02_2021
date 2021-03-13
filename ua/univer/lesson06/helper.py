class Helper:
    def input_int_from_console(self):
        while True:
            try:
                value = int(input("Enter int value"))
                return value
            except:
                print("Error not int")
