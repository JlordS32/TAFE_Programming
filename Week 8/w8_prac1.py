password = ['a', 'b', 'c']
password1 = input("Please enter your password:")
while password1 != password[0:1]:
    print("Wrong password.")
    password1 = input("Please enter the password: ")
print("Congrats")
