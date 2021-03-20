from ua.univer.lesson07.currency import Currency


class Product:
    def __init__(self,name,weight,price):
        self.name = name
        self.weight = weight
        self.price = price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if 0 < value < 100:
            self.__weight = value
        else:
            self.__weight = 0

    @property
    def price(self):
        return round(self.__price*Currency.eur*(1.20+0.10+0.10+0.10),2)

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value/Currency.eur
        else:
            self.__price = 0

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.price}"

    def __repr__(self):
        return f"Product ({self.name}, {self.weight}, {self.price})"