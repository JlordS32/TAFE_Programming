print("Welcome to the quiz.")
print("")
score = 0
totalMark = 5

q1 = input("What is the colour of an apple? ")
if (q1.casefold() == "red"):
    score = score + 1
    print("Correct!")
else:
    print("Wrong answer.")
print("")

q2 = input("is python a programming language or a snake?")
if (q2.casefold() == "both"):
    score = score + 1
    print("You're correct!")
elif q2.casefold() == "snake":
    print("You're partially correct.")
    score = score + 0.5
elif(q2.casefold() == "programming language"):
    print("You're partially correct.")
    score = score + 0.5
else:
    print("Wrong answer.")
print("")

q3 = int(input("10 + 10? "))
if q3 == 20:
    score = score + 1
    print("Correct!")
else:
    print("Wrong answer.")
print("")

q4 = input("AMD or Intel? ")
if q4.casefold() == "amd":
    score = score + 1
    print("Extra 1 point!.")
elif q4.casefold() == ("intel."):
    score = score + 0.5
    print(("A point for you :)"))
else:
    print("You have to choose one.")
print("")

q5 = input("Enter your name: ")
print("Hello", q5, "it was nice meeting you. Here's a free point just for you.")
score = score + 1
print("")

print("Your final mark:", score, "/", totalMark)
percent = score / 5 * 100
print("You got", percent, "%", "in marks.")

if (score >= 0) and (score <= 2):
    print("You got an F!")
elif score == 0:
    print("Try again! I believe in you!!")
elif (score > 2) and (score <= 3):
    print("You got a PASS!")
elif (score > 3) and (score <= 4):
    print("You got DISTINCTION!")
    print("You did your best!")
elif (score > 4) and (score <= 5):
    print("you got HIGH DISTINCTION!")
    print("")
    print("Congratulations! You did very well!")