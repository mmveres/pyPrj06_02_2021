from ua.univer.lesson06.helper import input_float_from_console


class Cat:
    def __init__(self, name="Tom", year=12, weight=7.5):
        self.__name = name
        self.__year = year
        self.__weight = weight
        self.mouse_list =[]

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.__year

    def set_weight(self, value):
        try:
            int_value = float(value)
            if 0<int_value<10:
                self.__weight = value
        except:
            print("error not float")

    def get_weight(self):
        return self.__weight

    def __str__(self):
        return f"Cat: {self.get_name()}, {self.get_year()}, {self.get_weight()}, {self.mouse_list}"


class CatDoctorController:
    __KITTEN_AGE = 1
    __MIDDLE_CAT = 5
    __OLD_CAT = 15

    def __init__(self, cat):
        self.cat = cat

    def diagnostic_age(self):
        if self.cat.get_year() < self.KITTEN_AGE:
            print("Kitten")
        elif self.cat.get_year() < self.MIDDLE_CAT:
            print("middle Cat")
        elif self.cat.get_year() < self.OLD_CAT:
            print("old Cat")


class CatEatController:
    def __init__(self, cat):
        self.cat = cat

    def max_food_limit(self):
        return self.cat.get_weight() / 2

    def min_food_limit(self):
        return 0

    def eat_mouse(self, mouse):
        self.eat(mouse.get_weight())
        self.cat.mouse_list.append(mouse)
        mouse.set_weight(0)
        mouse.set_killer(self.cat)

    def eat(self, food):
        if (self.min_food_limit() < food < self.max_food_limit()):
            self.cat.set_weight(self.cat.get_weight()+ food)
            return True
        else:
            print("Error food not in range (", self.min_food_limit(), "-", self.max_food_limit(), ")")
            return False

    def eat_from_console(self):
        while True:
            food = input_float_from_console()
            if self.eat(food):
                break
