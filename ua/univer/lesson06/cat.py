from ua.univer.lesson06.helper import Helper


class Cat:
    def __init__(self, name= "Tom", year= 12, weight= 7.5):
        self.name = name
        self.year = year
        self.weight = weight

    def print(self):
        print("*************")
        print("Cat :", self.name, self.year, self.weight)


class CatDoctorController:
    KITTEN_AGE = 1
    MIDDLE_CAT = 5
    OLD_CAT = 15
    def __init__(self, cat):
        self.cat = cat
    def diagnostic_age(self):
        if self.cat.year < self.KITTEN_AGE:
            print("Kitten")
        elif self.cat.year < self.MIDDLE_CAT:
            print("middle Cat")
        elif self.cat.year < self.OLD_CAT:
            print("old Cat")


class CatEatController:
    def __init__(self, cat):
        self.cat = cat

    def max_food_limit(self):
        return self.cat.weight/2

    def min_food_limit(self):
        return 0

    def eat(self, food):
        if (self.min_food_limit()<food<self.max_food_limit()):
            self.cat.weight+=food
            return True
        else:
            print("Error food not in range (", self.min_food_limit(),"-" ,self.max_food_limit(), ")")
            return False

    def eat_from_console(self):
        while True:
            food = Helper().input_int_from_console()
            if self.eat(food):
                break




