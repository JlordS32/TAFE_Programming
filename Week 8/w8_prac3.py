moni = 0
while moni <= 100:
    print("not enough moni")
    ans = input("do u wanna add more moni? ")
    if ans == "yes":
         moni1 = int(input("how much moni? "))
         moni = moni + moni1
         print("current balance:", moni)
    elif ans == "no":
        print("ok u don't want moni. bye")
        break
    elif moni >= 100:
        print("ok u have enough moni now")
        break
    else:
        print("fuck no")