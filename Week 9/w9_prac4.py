import random
game1 = ["rock", "paper", "scissor"]
score = 0
opponent_score = 0

game = input("Do you wanna play a game? ").lower()

while game != "yes":
    if game == "no":
        print("Understandable, goodbye.")
        quit()
    else:
        print("Please enter the proper command.")
    game = input("Do you wanna play a game? ").lower()

print("")
print("Welcome to the game!")
print("Do you wanna play [1. rock, paper, scissor] or [2. guess the number]? Please press either 1 or 2.")
n = ["1", "2"]
confirmation = input("Input: ")
while confirmation not in n:
    confirmation = input("Please press either 1 or 2: ")

if confirmation == n[0]:
    print("")
    print("So you wanna play rock, paper, and scissor. Okay.")
    print("Whoever gets the score of 2 wins!")
    while score != 2:
        ans = input("Please enter the command you wanna use [rock, paper or scissor]: ").lower()
        while ans not in game1:
            print("Please use the proper command.")
            ans = input("Input: ").lower()
        for i in random.sample(game1, 1): #random.sample randomly selects 1 string from the variable 'game1'
            if i == ans:
                print("Opponent:", i.upper())
                print("You:", ans.upper())
                print("TIE!")
            elif ans == game1[0] and i == game1[1]:
                print("Opponent:", i.upper())
                print("You:", ans.upper())
                opponent_score += 1
                print("You lost this round!")
                print("Your score: ", str(score) + "/2")
                print("Opponent score: ", str(opponent_score) + "/2")
            elif ans == game1[0] and i == game1[2]:
                print("Opponent:", i.upper())
                print("You:", ans.upper())
                score += 1
                print("You won this round!")
                print("Your score: ", str(score) + "/2")
                print("Opponent score: ", str(opponent_score) + "/2")
            elif ans == game1[1] and i == game1[0]:
                print("Opponent:", i.upper())
                print("You:", ans.upper())
                score += 1
                print("You won this round!")
                print("Your score: ", str(score) + "/2")
                print("Opponent score: ", str(opponent_score) + "/2")
            elif ans == game1[1] and i == game1[2]:
                print("Opponent:", i.upper())
                print("You:", ans.upper())
                opponent_score += 1
                print("You lost this round!")
                print("Your score: ", str(score) + "/2")
                print("Opponent score: ", str(opponent_score) + "/2")
            elif ans == game1[2] and i == game1[1]:
                print("Opponent:", i.upper())
                print("You:", ans.upper())
                score += 1
                print("You won this round!")
                print("Your score: ", str(score) + "/2")
                print("Opponent score: ", str(opponent_score) + "/2")
            elif ans == game1[2] and i == game1[0]:
                print("Opponent:", i)
                print("You:", ans)
                opponent_score += 1
                print("You lost this round!")
                print("Your score: ", str(score) + "/2")
                print("Opponent score: ", str(opponent_score) + "/2")
        if opponent_score == 2:
            print("You lost. Better try again next time.")
            quit()
    print("Congrats! You won!")

retry = 0
if confirmation == n[1]:
    print("")
    print("You'll have to guess random number.")
    num = random.randint(1, 10)
    guess = int(input("Guess the random number from 1 - 10: "))
    while guess != num:
        retry += 1
        print("Bad guess, the random number is", num)
        num = random.randint(1, 10)
        guess = int(input("Guess the random number: "))
        if guess == "no":
            print("Ok, you gave up.")
            print("Goodbye.")
            quit()
    print("Retries:", retry)
    print("Congrats! You got it right!")
