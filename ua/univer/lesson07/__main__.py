from ua.univer.lesson07.client import ClientAccount
from ua.univer.lesson07.currency import Currency
from ua.univer.lesson07.order import Order
from ua.univer.lesson07.product import Product

if __name__ == '__main__':

    apple = Product("Apple1", 2, 25)
    pineapple = Product("PineApple1", 1, 55)
    banana = Product("Banana1", 3, 35)
    client = ClientAccount("Tom",111)
    order = Order(client)
    order.add(apple)
    order.add(pineapple)
    order.add(banana)
    order2 = Order(client)
    order2.add(Product("Tomato", 1, 40))
    Currency.usd = 30
    order.print()
    print("max price=",order.get_max_price())
    print("max weight=",order.get_max_weight())
    print("total price =", order.get_total_price())
    print("total price with discount =", order.get_total_price_with_discount())
    print(client.order_list)
    print(order)