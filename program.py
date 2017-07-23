from classes import Bicycle, BikeShop, Customer
import pprint


bike0 = Bicycle("Trek FUEL EX 9.7 29", 25, 2000)
bike1 = Bicycle("Specialized PITCH COMP 650B", 30, 300)
bike2 = Bicycle("Trek MARLIN 4", 45, 150)
bike3 = Bicycle("Specialized REMEDY", 30, 1000)
bike4 = Bicycle("Specialized CYCLONE", 50, 400)
bike5 = Bicycle("Trek TISKER", 45, 50)

#print("bike0 is {}".format(bike0))

bss = BikeShop("Bicycle Sports")

print(bss)

bikes = [bike0, bike1, bike2, bike3, bike4, bike5]
for bike in bikes:
    bss.stock(bike)

pprint.pprint(bss.inventory)

pprint.pprint(bss.count())

# # bss.sell(bike5)
# print(bss)

# for item in bss.inventory:
#     print(item)

# print(bss.sell(bike5))
# print(bss.sell(bike4))

