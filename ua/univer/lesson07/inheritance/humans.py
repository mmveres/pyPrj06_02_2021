class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.profession = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            self.__age = 0

    def __str__(self):
        return f"{self.name}, {self.age}"

class Student(Human):
    def __init__(self, name, age, id_group):
        Human.__init__(self,name,age)
        self.id_group = id_group
        self.profession = "Study"

    def __str__(self):
        return f"{super().__str__()}, {self.id_group}"


class Doctor(Human):
    def __init__(self, name, age, id_licence):
        super().__init__(name, age)
        self.id_licence = id_licence
        self.profession = "Cure"


class Fighter(Human):
    def __init__(self, name, age, power, defence):
        super().__init__(name, age)
        self.power = power
        self.defence = defence
        self.profession = "Fight"
