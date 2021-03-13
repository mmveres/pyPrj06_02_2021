from ua.univer.lesson06.cat import *
from ua.univer.lesson06.helper import Helper

if __name__ == '__main__':
    cat1 = Cat()
    cat1.print()
    cat_eating = CatEatController(cat1)
    cat_eating.eat_from_console()
    cat1.print()

    cat_diag = CatDoctorController(cat1)
    cat_diag.diagnostic_age()

    cat2 = Cat("Tom2", 5, 5.6)
    cat2.print()
    CatDoctorController(cat2).diagnostic_age()

    cat3 = Cat(weight=4.6, name="Tom3",year=6)
    cat3.print()
    CatDoctorController(cat3).diagnostic_age()