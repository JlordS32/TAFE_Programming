""" THE DEF FUNCTION TEST"""

def my_cats(cat1, cat2):
    print("I like", cat1, "but I like", cat2, "better.")

cat1 = input("What's the first name of the cat? ")
cat2 = input("Second name of the cat: ")
my_cats(cat1, cat2)

def multiply_two_numbers(a, b):
    c = a * b
    return c

print(multiply_two_numbers(2, 2))

def stuff_from_store(amount, stuff, store):
    print("I really need", amount, stuff, "from the", store)

def tires_needed(cars):
    tires = multiply_two_numbers(cars, 4)
    stuff_from_store(tires, "tires", "tire shop")

cars = int(input("How many cars do you have? "))
tires_needed(cars)