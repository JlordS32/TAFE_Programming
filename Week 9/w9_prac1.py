import random

weather = ["sunny", "cloudy", "rainy", "drizzling", "storm"]
current_weather = []
arrival = ["late", "early", "on time"]
current_arrival = []

for i in range(1):
    w1 = random.randint(1, 5)
    if w1 == 1:
        current_weather.append(weather[0])
    elif w1 == 2:
        current_weather.append(weather[1])
    elif w1 == 3:
        current_weather.append(weather[2])
    elif w1 == 4:
        current_weather.append(weather[3])
    elif w1 == 5:
        current_weather.append(weather[4])

for i in range(1):
    c1 = random.randint(1, 3)
    if c1 == 1:
        current_arrival.append(arrival[0])
    elif c1 == 2:
        current_arrival.append(arrival[1])
    elif c1 == 3:
        current_arrival.append(arrival[2])


print("Should I go to work?")
checking = input("What's the weather today? ").lower()
if checking == current_weather[0]:
    print("Okay it's", current_weather[0] + ".")
else:
    if current_weather[0] == weather[4]:
        print("Okay it's not", checking + ".", "as there will be", current_weather[0])
    else:
        print("Okay it's not", checking + ".", "as it'll be", current_weather[0])

checking2 = input("Will I be late, early or on time? ").lower()
if checking2 == current_arrival[0]:
    print("Okay I think I'll be", current_arrival[0] + ".")
else:
    print("Okay I won't be", checking2, "as I'll be", current_arrival[0] + ".")

print("")
print("Now, should I go to work? ")
if current_weather[0] == weather[0] and current_arrival[0] == arrival[0]:
    print("I can still go to work.")
elif current_weather[0] == weather[0] and current_arrival[0] == arrival[1]:
    print("I should be able to work and do some stuff along the way.")
elif current_weather[0] == weather[0] and current_arrival[0] == arrival[2]:
    print("I'll make it in time.")
elif current_weather[0] == weather[1] and current_arrival[0] == arrival[0]:
    print("I can still go to work. It's just cloudy.")
elif current_weather[0] == weather[1] and current_arrival[0] == arrival[1]:
    print("I should be able to work and do some stuff along the way.")
elif current_weather[0] == weather[1] and current_arrival[0] == arrival[2]:
    print("I'll make it in time. It's only cloudy.")
elif current_weather[0] == weather[3] and current_arrival[0] == arrival[0]:
    print("I can still go to work. It's just drizzling")
elif current_weather[0] == weather[3] and current_arrival[0] == arrival[1]:
    print("I should be able to work but I might be limited to some stuff along the way.")
elif current_weather[0] == weather[3] and current_arrival[0] == arrival[2]:
    print("I'll make it in time for sure. Gotta be careful though.")
else:
    print("Too lazy~ I'm staying home...")
