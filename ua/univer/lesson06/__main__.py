from datetime import datetime

from ua.univer.lesson06.cat import *
from ua.univer.lesson06.mouse import Mouse

if __name__ == '__main__':
    now = datetime.now()
    print(str(now))
    print(repr(now))
    cat1 = Cat()
    cat1.set_weight(10.1)
    print(cat1)

  #  cat_eating = CatEatController(cat1)
  #  cat_eating.eat_from_console()
  #  print(cat1)

    cat_diag = CatDoctorController(cat1)
    cat_diag.diagnostic_age()

    cat2 = Cat("Tom2", 5, 5.6)
    print(cat2)
    CatDoctorController(cat2).diagnostic_age()

    cat3 = Cat(weight=4.6, name="Tom3",year=6)
    print(cat3)
    CatDoctorController(cat3).diagnostic_age()

    mouse1 = Mouse("Jerry", 0.3)
    mouse1.print()
    print(mouse1)
    print(str(mouse1))
    print(repr(mouse1))

    CatEatController(cat1).eat(3)
    print(cat1)
    mouse1.set_killer(cat2)
    print(mouse1)
    CatEatController(cat1).eat_mouse(mouse1)
    print(mouse1)
    CatEatController(cat1).eat_mouse(Mouse("Anonim", 0.5))
    print(cat1)