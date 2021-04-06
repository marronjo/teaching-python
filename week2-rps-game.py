#Game of Rock, Paper, Scissors
#Take input from the user e.g rock, paper or scissors   DONE
#Generate the computer's response                       DONE
#Who wins
import random

guess = input("Rock Paper or Scissors: ")

f = random.randint(1,3)

if f == 1:
    tucom = "Rock"
elif f == 2:
    tucom = "Paper"
elif f == 3:
    tucom = "Scissors"
else:
    print("Error Incorrect!")

print("Your Guess: "  + guess)
print("The Computer's Guess: "  + tucom)

#variable guess used for user's turn
#variable tucom used for computer's turn

if guess == tucom
    print("Draw! Try again")
elif guess == "Rock" and tucom == "Paper"
    print("You Lose!!")
elif guess == "Rock" and tucom == "Scissors"
    print("You Win!!")
elif guess == "Paper" and tucom == "Scissors"
    print("You Lose!!")
elif guess == "Paper" and tucom == "Rock"
    print("You Win!!")
elif guess == "Scissors" and tucom == "Rock"
    print(You Lose!!)
elif guess == Scissors and tucom == Paper
    print(You Win!!)
else
    print(Error Try Again!)
