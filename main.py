from bicycles import Bicycle, BikeShop, Customer
import random


def main():
    print_header()
    # Create 6 different bicycle models
    bike0 = Bicycle("Trek FUEL EX 9.7 29", 25, 800)
    bike1 = Bicycle("Specialized PITCH COMP 650B", 30, 300)
    bike2 = Bicycle("Trek MARLIN 4", 45, 150)
    bike3 = Bicycle("Specialized REMEDY", 30, 600)
    bike4 = Bicycle("Specialized CYCLONE", 50, 75)
    bike5 = Bicycle("Trek TISKER", 45, 100)
    print()
    
    # Create bicycle shop
    bss = BikeShop("Bicycle Sports Shop")
    print()
    # Stock the shop with the bicycles. The shop should charge 
    # its customers 20% over the cost of the bikes.
    bikes = [bike0, bike1, bike2, bike3, bike4, bike5]
    for bike in bikes:
        bss.stock(bike, 5, 0.2)  # 5 bikes of one model added to shop's stock
    print()

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
    customer_rec_bikes = {}    # create dict for rec bikes/customer
    for customer in customers:
        #print(customer.name)
        recommended_bikes = recommend_bikes(customer, bss)
        recommended_models = [bike["model"] for bike in recommended_bikes]
        recommended_models = set(recommended_models)
        customer_rec_bikes[customer.name] = recommended_bikes   
        print("Recommended bikes for {}".format(customer.name))
        for bike in recommended_models:
            print(bike)
        print()
        
    # Print the initial inventory of the bike shop for each bike it carries.
    # print("Initial inventory of {}:".format(bss.name))
    print("{}'s initial inventory:".format(bss.name))
    for key, value in bss.count().items():
        print("{}: {} available".format(key, value))
    print()
    
    # Have each of the three customers purchase a bike then print
    # the name of the bike the customer purchased, the cost,
    # and how much money they have left over in their bicycle fund.
    for customer in customers:
        bike_choice = random.choice(customer_rec_bikes[customer.name])
        print("{}'s choice: {}".format(customer.name, bike_choice["model"]))
        bike = Bicycle(model=bike_choice["model"], weight = bike_choice["weight"], cost=bike_choice["cost"])
        customer.buy(1, bike, bss)
        print()
        
    # After each customer has purchased their bike, the script should
    # print out the bicycle shop's remaining inventory for each bike, 
    # and how much profit they have made selling the three bikes.
    print("{}'s inventory after sale:".format(bss.name))
    for key, value in bss.count().items():
        print("{}: {} available".format(key, value))
    print()
    print("{}'s profit after today's sale:\n${:.2f}".format(bss.name, bss.profit))


def print_header():
    print("----------------------------------")
    print("  BICYCLE INDUSTRY MODEL APP")
    print("----------------------------------")
    print()


def recommend_bikes(customer, shop):
    """Recommend bikes to customer based on customer fund"""
    recommended_bikes = []
    for bike in shop.inventory:
        if customer.fund >= bike["price"]:
            recommended_bikes.append(bike)
    return recommended_bikes


if __name__ == "__main__":
    main()

