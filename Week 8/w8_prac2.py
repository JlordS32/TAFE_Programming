counter = 1
while (counter < 5):
    if counter < 2:
        print('Less than 2')
    elif counter > 4:
        print('Greater than 4')
    counter += 1

special_food = ["avocado", "eggs"]
food = input("food: ").lower()
while (food != "banana"):
    print("it's not a banana.")
    print("it is a", food)
    if food == "apple":
        print("Oh, it is an apple!.")
        apple = input("do you want to cut it? yes/no: ").lower()
        if apple == "yes":
            print("you cut nice.")
        elif apple == "no":
            print("fuck you.")
        else:
            print("ok")
    elif food in special_food:
        if food == special_food[0]:
            print("yuckkkkk.")
        elif food == special_food[1]:
            print("protein mannn.")
    food = input("again:")
print("it is a banana")

