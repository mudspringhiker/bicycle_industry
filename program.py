from industry import Bicycle, BikeShop

bike0 = Bicycle("Trek", "FUEL EX 9.7 29", 25, 2000)
bike1 = Bicycle("Specialized", "PITCH COMP 650B", 30, 300)
bike2 = Bicycle("Trek", "MARLIN 4", 45, 150)
bike3 = Bicycle("Specialized", "REMEDY", 30, 1000)
bike4 = Bicycle("Specialized", "CYCLONE", 50, 400)
bike5 = Bicycle("Trek", "TISKER", 45, 50)

inventory = [bike0, bike1, bike2, bike3, bike4, bike5]
# print(bike0.brand, bike0.cost, bike0.model, bike0.weight)
for bike in inventory:
    print(bike.describe())
    
    
bss = BikeShop("Bicycle Sports")

print(bss.describe())

bss.inventory = inventory

print(bss.sell(bike0))

