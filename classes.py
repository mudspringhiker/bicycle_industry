from collections import Counter


class Bicycle():
    '''
    Bicycle class has model, weight, and cost of production
    '''
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        self.price = 0
        print("Bicycle {} created".format(self.model))
        
    def __repr__(self):
        return "Bicycle: {}, {}".format(self.model, self.weight)
        
    def dict_(self):
        """Returns the bicycle in a dictionary form"""
        bike_info = {}
        bike_info["model"] = self.model
        bike_info["weight"] = self.weight
        bike_info["cost"] = self.cost
        return bike_info
      

class BikeShop:
    '''
    BikeShop has name, inventory of different bikes, sell bikes 
    with a margin over their costs, can see how much profit
    they have made from selling bikes
    '''
    def __init__(self, name):
        self.name = name # name of the bike shop
        self.inventory = [] # a list of dictionaries containing bike info
        self.profit = 0 # tracks the total profit of the bike shop
        print("Bicycle shop {} created!".format(self.name))

    def __repr__(self):
        if self.inventory:
            return "Shop name: {}".format(self.name)
        else:
            return "Shop name: {} NOTE: No item in stock".format(self.name)

    def stock(self, bike):
        """Returns the inventory of the shop after adding a bicycle
        to the inventory."""
        self.inventory.append(bike.dict_())
        return self.inventory
        
    def count(self):
        """Counts the number of bike models in stock"""
        record = [bike["model"] for bike in self.inventory]
        return Counter(record)
    
    def sell(self, bike):
        if bike in self.inventory:
            bike_i = self.inventory.index(bicycle)
            del self.inventory[bike_i]
            # bike_price = bicycle.cost + bicycle.cost * 0.20
            self.profit += (bicycle.price - bicycle.cost)
            return "{} sold.\nProfit: ${:.2f}".format(bicycle, self.profit)
        else:
            return "Bicycle not in stock."
            

class Customer:
    '''
    Customer has name, fund to buy bike, can buy and own bike
    '''
    # pass
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        
    def buy(self, bike):
        if self.fund >= bike.price:
            self.fund += bike.price
            print("{} bought a bike!".format(self.name))
            return self.fund
        else:
            return("You don't have enough funds!")
            
    
        