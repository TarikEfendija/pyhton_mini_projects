# We create a program for rock, paper, scissors game
# User will play against computer 5 times and program will say to us who have more wins. 

import random

user_wins=0
comp_wins=0
set = 0

options = ["rock", "paper", "scissors"]

while True:

    user_input= input("Type rock or paper or scissors: ").lower()
    if user_input not in options:
        print("You have to pick rock or paper or scissors!")
        continue

    random_number = random.randint(0,2)
    comp_pick= options[random_number]

    print("Computer picked", comp_pick + ".")

    


    if user_input == "rock" and comp_pick == "scissors":
        print("You won this set!")
        user_wins += 1
        set +=1
    
    elif user_input == "paper" and comp_pick == "rock":
        print("You won this set!")
        user_wins += 1
        set+=1
    
    elif user_input == "scissors" and comp_pick == "paper":
        print("You won this set!")
        user_wins += 1
        set+=1
    
    elif user_input == comp_pick:
        print("Drow")
        set +=1
    else:
        print("You lost this set!")
        comp_wins += 1
        set +=1
    if set > 4:
        break

if user_wins > comp_wins:
     print("You won the game!")
else:
    print("Sorry, you lost the game. Better luck next time.")
