from bicycles import Bicycle, BikeShop, Customer
import pprint
import random

def main():
    # Create 6 different bicycle models
    bike0 = Bicycle("Trek FUEL EX 9.7 29", 25, 800)
    bike1 = Bicycle("Specialized PITCH COMP 650B", 30, 300)
    bike2 = Bicycle("Trek MARLIN 4", 45, 150)
    bike3 = Bicycle("Specialized REMEDY", 30, 600)
    bike4 = Bicycle("Specialized CYCLONE", 50, 75)
    bike5 = Bicycle("Trek TISKER", 45, 100)
    
    # Create bicycle shop
    bss = BikeShop("Bicycle Sports")
    
    # Stock the shop with the bicycles. The shop should charge 
    # its customers 20% over the cost of the bikes.
    bikes = [bike0, bike1, bike2, bike3, bike4, bike5]
    for bike in bikes:
        bss.stock(bike, 5)  # 5 bikes of one model added to shop's stock

    # Create three customers. One customer has a budget of $200, 
    # the second $500, and the third $1000.
    customer1 = Customer("Joe", 200)
    customer2 = Customer("Jen", 500)
    customer3 = Customer("Jerry", 1000)

    # Print the name of each customer, and a list of the bikes offered 
    # by the bike shop that they can afford given their budget. 
    # Make sure you price the bikes in such a way that each customer 
    # can afford at least one.
    customers = [customer1, customer2, customer3]
    for customer in customers:
        print(customer.name)
        rec_bikes = recommend_bikes(customer, bss)
        print("Recommended bikes for {}".format(customer.name))
        for bike in rec_bikes:
            print(bike)
        
    # Print the initial inventory of the bike shop for each bike it carries.
    print("Initial inventory of the bike shop")
    pprint.pprint(bss.count())
    
    # Have each of the three customers purchase a bike then print
    # the name of the bike the customer purchased, the cost,
    # and how much money they have left over in their bicycle fund.
    
    
    




# After each customer has purchased their bike, the script should
# print out the bicycle shop's remaining inventory for each bike, 
# and how much profit they have made selling the three bikes.




# print()
# print("{}'s inventory:".format(bss.name))
# for item in bss.inventory:
#     print(item)
# print()
# print("Numbers of bikes in inventory per model:")
# pprint.pprint(bss.count())
# print()
# bss.stock(bike5, 2)
# pprint.pprint(bss.count())
# print()
# bss.sell(bike5, 1)
# pprint.pprint(bss.count())
# print()
# print(bss.profit)
# bss.sell(bike0, 1)
# pprint.pprint(bss.count())
# print(bss.profit)
# print()
# joe = Customer("Joe", 4000)
# print(joe)
# print()
# joe.buy(1, bike2, bss)
# pprint.pprint(bss.count())

def recommend_bikes(customer, shop):
    """Recommend bikes to customer based on customer fund"""
    recommended_bikes = []
    for bike in shop.inventory:
        if customer.fund >= bike["price"]:
            recommended_bikes.append(bike)
    return recommended_bikes


if __name__ == "__main__":
    main()

