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
        print("Bicycle shop {} created!".format(self.name))

    def __repr__(self):
        if self.inventory:
            return "Shop name: {}".format(self.name)
        else:
            return "Shop name: {}\nNo item in stock".format(self.name)

    def stock(self, bike):
        """Returns the inventory of the shop after acquiring bikes to sell."""
        bike_info = {}
        bike_info["model"] = bike.model
        bike_info["weight"] = bike.weight
        bike_info["cost"] = bike.cost
        self.inventory.append(bike_info)
        return self.inventory
        
    def count(self):
        """Counts the number of bike models in stock"""
        record = [bike["model"] for bike in self.inventory]
        return Counter(record)
    
    def sell(self, bicycle, customer):
        if bicycle in self.inventory and customer.fund >= bicycle.price:
            bike_i = self.inventory.index(bicycle)
            del self.inventory[bike_i]
            # bike_price = bicycle.cost + bicycle.cost * 0.20
            self.profit += (bicycle.price - bicycle.cost)
            return "{} sold.\nProfit: ${:.2f}".format(bicycle, self.profit)
        else:
            return "Bicycle not in stock."
            

class Customer:
    '''
    Customer has name, have fund to buy bike, can buy and own bike
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
            
    
        