num = int(input("Enter a number: "))
print("The number is", num)
if num % 4 == 0:
    print(num, "is divisible by 4.")
if num % 2 == 0:
    print(num, "is divisible by 2.")
else:
    print(num, "is an odd number.")