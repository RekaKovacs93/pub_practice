class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drink_stock = [] #shelf


    # def add_drink_to_stock (self, drink):
        # self.drink_stock.append(drink)

    def sell_a_drink(self, customer, drink):
        self.till += drink.price #self.till = self.till + drinks.price
        customer.wallet -= drink.price
        # self.drink_stock.remove(drink)

    

    