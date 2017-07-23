from classes import Bicycle, BikeShop, Customer
import pprint


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

