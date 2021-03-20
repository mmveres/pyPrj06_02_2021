class Order:
    def __init__(self, client_account):
        self.client_account = client_account
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

    def get_total_price(self):
        sum_price =0
        for product in self.__product_list:
            sum_price += product.price
        return sum_price

    def get_total_price_with_discount(self):
        return self.get_total_price()*(1-self.client_account.discount/100)

    def print(self):
        for product in self.__product_list:
            print(product)

    def complite(self):
        self.print()
        if self.client_account.bank_account > self.get_total_price_with_discount():
            self.client_account.bank_account - self.get_total_price_with_discount()
            self.client_account.order_list.append(self)

    def __str__(self):
        return str(self.__product_list)

    def __repr__(self):
        return repr(self.__product_list)