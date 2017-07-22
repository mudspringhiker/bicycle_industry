# Bicycle, shops and customers

class Bicycle():
    '''
    Bicycle class has model, weight, and cost of production
    '''
    def __init__(self, brand, model, weight, cost):
        self.brand = brand
        self.model = model
        self.weight = weight
        self.cost = cost
        
    def describe(self):
        '''Returns the description of the bike'''
        name = "{}, model {}, {}lbs, ${}".format(self.brand, self.model, self.weight, self.cost)
        return name


class BikeShop:
    '''
    BikeShop has name, inventory of different bikes, sell bikes 
    with a margin over their costs, can see how much profit
    they have made from selling bikes
    '''
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.profit = 0

    def describe(self):
        return self.name
        
    def sell(self, bicycle):
        if bicycle in self.inventory:
            bike_i = self.inventory.index(bicycle)
            del self.inventory[bike_i]
            bike_price = bicycle.cost + bicycle.cost * 0.20
            self.profit += (bike_price - bicycle.cost)
            return self.inventory, self.profit
        else:
            return "Bicycle not in stock."
            

class Customer:
    '''
    Customer has name, have fund to buy bike, can buy and own bike
    '''
    pass