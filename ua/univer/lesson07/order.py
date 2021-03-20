class Order:
    def __init__(self):
        self.__product_list = []

    def add(self, product):
        self.__product_list.append(product)

    def get_max_weight(self):
        max_weight_product = self.__product_list[0]
        for product in self.__product_list:
            if product.weight > max_weight_product.weight:
                max_weight_product = product
        return max_weight_product

    def get_max_price(self):
        max_price_product = self.__product_list[0]
        for product in self.__product_list:
            if product.price > max_price_product.price:
                max_price_product = product
        return max_price_product

    def print(self):
        for product in self.__product_list:
            print(product)