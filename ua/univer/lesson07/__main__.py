from ua.univer.lesson07.currency import Currency
from ua.univer.lesson07.order import Order
from ua.univer.lesson07.product import Product

if __name__ == '__main__':

    apple = Product("Apple1", 2, 25)
    pineapple = Product("PineApple1", 1, 55)
    banana = Product("Banana1", 3, 35)

    order = Order()
    order.add(apple)
    order.add(pineapple)
    order.add(banana)
    order.add(Product("Tomato", 1, 40))
    Currency.usd = 30
    order.print()
    print("max price=",order.get_max_price())
    print("max weight=",order.get_max_weight())