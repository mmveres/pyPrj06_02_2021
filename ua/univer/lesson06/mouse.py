class Mouse:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight
        self.__killer = None

    def get_name(self):
        return self.__name

    def set_weight(self, value):
        self.__weight = value

    def get_weight(self):
        return self.__weight

    def set_killer(self, killer):
        if self.get_weight()<=0:
            self.__killer = killer
            print("kill successes by", killer)
        else:
            print(killer, "no kill no killer")

    def get_killer(self):
        return self.__killer

    def print(self):
        print("*************")
        print("Mouse :", self.__name, self.__weight)

    def __str__(self):
        if self.get_weight()>0:
            return f"{self.get_name()}, {self.get_weight()}"
        else:
            return f"{self.get_name()}......RIP...... kill by {self.get_killer()}"

    def __repr__(self):
        return f"Mouse({self.__name}, {self.__weight})"