class Coffee:
    name = ''
    price = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def rename(self, name=''):
        self.name = name

    def set_price(self, price=0):
        self.price = price

    def __str__(self):
        return f"[{self.name}, 가격: {self.price}]"

