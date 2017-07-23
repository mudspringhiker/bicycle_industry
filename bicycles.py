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
        print("Bicycle {} created!".format(self.model))
        
    def __repr__(self):
        return "Bicycle: {}".format(self.model)
        
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
            return "Shop name: {} NOTE: No items in stock".format(self.name)

    def stock(self, bike, number_of_bikes):
        """Returns the inventory of the shop after adding 'number_of_bikes'
        bicycle to the inventory."""
        bike.price = bike.cost + bike.cost * 0.20
        bike_info = bike.dict_()
        bike_info["price"] = bike.price
        for i in range(number_of_bikes):
            self.inventory.append(bike_info)
        print("{} {} added to shop inventory.".format(number_of_bikes, bike))
        return self.inventory
        
    def count(self):
        """Counts the number of bike models in stock"""
        record = [bike["model"] for bike in self.inventory]
        return Counter(record)
    
    def sell(self, bike, n):
        """Updates the shop's inventory after selling n number of bike."""
        #print(bike.dict_()["model"])
        #print(self.inventory)
        inventory_models = [item["model"] for item in self.inventory]
        for i in range(n):
            if bike.model in inventory_models:
                # print(True)
                for i, model in enumerate(inventory_models):
                    if model == bike.model:
                        del self.inventory[i]  # delete the sold bike from inventory
                        break                  # delete only for first one found
                self.profit += (bike.price - bike.cost)
                print("{} sold and removed from inventory. Profit added to total.".format(bike))
                return self.inventory, self.profit
            else:
                return "Bicycle not in stock."
            

class Customer:
    '''
    Customer has name, fund to buy bike, can buy and own bike
    '''
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        
    def __repr__(self):
        return "{} with ${}".format(self.name, self.fund)
        
    def buy(self, n, bike, bikeshop):
        """Returns customer funds, bikeshop inventory after 
        customer buys n number of bike from bikeshop."""
        if self.fund >= bike.price:
            self.fund -= bike.price
            bikeshop.sell(bike, n)
            print("{} bought a bike!".format(self.name))
            print("{} has ${:.2f} remaining funds.".format(self.name, self.fund))
            return self.fund, bikeshop
        else:
            return("You don't have enough funds!")
