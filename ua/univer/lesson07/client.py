class ClientAccount:
    def __init__(self, name, account, bank_account):
        self.name = name
        self.account = account
        self.bank_account = bank_account
        self.order_list = []

    def sum_price_order(self):
        sum_price=0
        for order in self.order_list:
            sum_price+=order.get_total_price()
        return sum_price

    @property
    def discount(self):
        sum_price = self.sum_price_order()
        if sum_price < 100:
            return 5
        elif sum_price < 1000:
            return 7
        elif sum_price < 10000:
            return 10
        else:
            return 12