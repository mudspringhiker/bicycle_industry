from bicycles import Bicycle, BikeShop, Customer
import pprint


# Create a bicycle shop that has 6 different bicycle models in stock. 
# The shop should charge its customers 20% over the cost of the bikes.


# Create three customers. One customer has a budget of $200, 
# the second $500, and the third $1000.

# Print the name of each customer, and a list of the bikes offered 
# by the bike shop that they can afford given their budget. 
# Make sure you price the bikes in such a way that each customer 
# can afford at least one.

# Print the initial inventory of the bike shop for each bike it carries.

# Have each of the three customers purchase a bike then print
# the name of the bike the customer purchased, the cost,
# and how much money they have left over in their bicycle fund.

# After each customer has purchased their bike, the script should
# print out the bicycle shop's remaining inventory for each bike, 
# and how much profit they have made selling the three bikes.

bike0 = Bicycle("Trek FUEL EX 9.7 29", 25, 2000)
bike1 = Bicycle("Specialized PITCH COMP 650B", 30, 300)
bike2 = Bicycle("Trek MARLIN 4", 45, 150)
bike3 = Bicycle("Specialized REMEDY", 30, 1000)
bike4 = Bicycle("Specialized CYCLONE", 50, 400)
bike5 = Bicycle("Trek TISKER", 45, 50)
print()
#print("bike0 is {}".format(bike0))

bss = BikeShop("Bicycle Sports")
print()

bikes = [bike0, bike1, bike2, bike3, bike4, bike5]
for bike in bikes:
    bss.stock(bike, 1)
print()
print("{}'s inventory:".format(bss.name))
for item in bss.inventory:
    print(item)
print()
print("Numbers of bikes in inventory per model:")
pprint.pprint(bss.count())
print()
bss.stock(bike5, 2)
pprint.pprint(bss.count())
print()
bss.sell(bike5, 1)
pprint.pprint(bss.count())
print()
print(bss.profit)
bss.sell(bike0, 1)
pprint.pprint(bss.count())
print(bss.profit)
print()
joe = Customer("Joe", 4000)
print(joe)
print()
joe.buy(1, bike2, bss)
pprint.pprint(bss.count())

