#VARIABLES
import sys

balance = 20
egg_cost = 0
pizza_cost = 0
salad_cost = 0
total_cost = 0
menu = ["eggs", "pizza", "salad"]
egg_type = ["boiled", "fried", "request"]
pizza_topping = ["meat", "chicken", "pineapple", "request"]
extra = []

#NAME
name = input("Hello, may I know your name? ")
if name.casefold() == "no":
    print("That's sad, you don't want to introduce yourself. Oh well")
    print("Goodbye.")
    sys.exit()
print("")

print("Good morning", name, "welcome to the restaurant.")
confirmation = input("Would you like to order? yes/no:  ").lower()
while confirmation != "no":
        if confirmation == "yes":
            print("")
            print("What would you like to order? ")
            print("As for our menu for today, we have eggs, pizza, and salad.")
            order = input("Please choose which one: ").lower()
            if order in menu:
#EGGS
                if order == menu[0]:
                    egg_cost += 5
                    print("Eggs for breakfast sounds ideal to me.")
                    order1 = input("Would you like it boiled, fried or do you wanna make a request? ").lower()
                    if order1 == egg_type[0]:
                        print("Alright, I'll have it boiled for you, please wait.")
                        print("")
                    elif order1 == egg_type[1]:
                        egg_cost += 1
                        print("Ohh, I love fried eggs!")
                        print("")
                    elif order1 == egg_type[2]:
                        egg_cost += 2.5
                        extra.append(input("What do you wanna request? "))
                        print("Alright, I'll have your", extra[0], "ready asap.")
                        print("")
                    else:
                        print("I'm sorry we currently don't have that in the menu.")
                        print("")
#PIZZA
                elif order == menu[1]:
                    pizza_cost += 2.5
                    print("Pizza for the morning sounds nice, but not too much.")
                    slices = int(input("How many slices of pizza do you want? "))
                    pizza_cost = slices * pizza_cost
                    print(slices, "slices of pizza alright.")
                    print("What toppings would you like for your pizza? We currently have meat, chicken and pineapple.")
                    order1 = input("Please choose which one: ").lower()
                    if order1 == pizza_topping[0]:
                        pizza_cost += 0.5
                        print("Meat pizza coming right up!")
                        print("")
                    elif order1 == pizza_topping[1]:
                        pizza_cost += 0.75
                        print("Chicken pizza coming right up!")
                        print("")
                    elif order1 == pizza_topping[2]:
                        pizza_cost += 0.2
                        print("Hawaiian pizza alright.")
                        print("")
                    else:
                        print("I'm sorry we currently don't have that in the menu.")
                        print("")
#SALAD
                elif order == menu[2]:
                    salad_cost += 10
                    print("Going for the healthy option are we?")   #a salad is salad. no ifs
                    print("")

            else:
                print("I'm sorry to say this, but we don't have that in the menu.")
                print("")

        confirmation = input("Do you still want to order? ").lower()
        if confirmation == "no":
            total_cost = pizza_cost + salad_cost + egg_cost
            balance = balance - total_cost
            print("That'll be", total_cost, "please.")
            print("Current Balance:", balance)
            if balance < 0:
                print("Insufficient balance, unfortunately you don't have enough balance to afford this order.")
            else:
                print("Thanks for ordering, please kindly wait until your food is ready.")
                break
print("Thanks for coming.")
