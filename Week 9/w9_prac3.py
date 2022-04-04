import random
import sys

weather = ["sunny", "cloudy", "rainy"]
arrival = ["on time", "early", "late"]

print("Should I go to work?")
checking = input("What's the weather today? ").lower()
while checking not in weather:
    if checking == "no":
        print("Lazy bastard, check the weather.")
        checking = input("So, what's the weather? ").lower()
        if checking == "no":
            print("CHECK THE WEATHER!!")
            input("Weather: ")
            if checking == "no":
                print("AAAAAAAAAAA")
                sys.exit()
    else:
        print("Invalid command. Do it again")
        checking = input("What's the weather today? ").lower()
checking2 = input("Will I be on time, early, or late? ").lower()
while checking2 not in arrival:
    print("Invalid command.")
    checking2 = input("Will I be on time, early, or late? ").lower()

for cw in random.sample(weather, 1):
    if checking == cw:
        print("Okay it's", cw + ".")
    else:
        print("It's not", checking, "as It'll be", cw)
for ca in random.sample(arrival, 1):
    if checking2 == ca:
        if ca == arrival[0]:
            print("Ok, I'll be", ca + ".")
        elif ca == arrival[1]:
            print("I'll be pretty", ca + ".")
        elif ca == arrival[2]:
            print("I'll be", ca + ".")
    else:
        print("Okay, I won't be", checking2, "as I'll be", ca + ".")

print("")
print("Now, should I go to work?")
if cw in weather[0] and ca in arrival:
    print("I should be able to go to work.")
if cw in weather[1] and ca in arrival:
    print("I should be able to go to work. It's just cloudy")
else:
    print("Can't go to work for today.")