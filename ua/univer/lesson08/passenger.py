import abc


class Passenger():
    def __init__(self, count_pass):
        self.count_pass = count_pass

    @property
    def count_pass(self):
        return self.__count_pass

    @count_pass.setter
    def count_pass(self, value):
        if value > 0:
            self.__count_pass = value
        else:
            self.__count_pass = 0


    def show_image(self):
        print("Passenger")