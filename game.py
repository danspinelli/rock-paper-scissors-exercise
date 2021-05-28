# game.py

import random
import os
import dotenv

dotenv.load_dotenv()

Player_Name = os.getenv("Player_Name")


#can separate strings with commas
#print("Welcome", Player_Name,"! Rock, Paper, Scissors, Shoot!")

#or we can concatenate with "+"

print("Welcome " + Player_Name +"! Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

print("User Choice: ", user_choice)

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
    exit()


valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)

print("Computer choice: ", computer_choice)


#This was my way to write this code

#if (user_choice == "rock" and computer_choice == "paper"):
#   print("Computer Wins")
#elif (user_choice == "paper" and computer_choice == "rock"):
#       print("User Wins")
#elif (user_choice == "scissors" and computer_choice == "rock"):
#         print("Computer Wins")
#elif (user_choice == "scissors" and computer_choice == "paper"):
#        print("User Wins")
#elif (user_choice == "rock" and computer_choice == "scissors"):
#         print("User Wins")
#elif (user_choice == "paper" and computer_choice == "scissors"):
#        print("Computer Wins")
#else:
#    print("Tie, Play Again")


#This is a better way to do it because it is less redundant

if user_choice == computer_choice:
    print ("Tie, Play Again")
if user_choice == "rock":
    if computer_choice == "rock":
        print("IT'S A TIE")
    elif computer_choice == "paper":
        print("OH, THE COMPUTER WON...")
    elif computer_choice == "scissors":
        print("YOU WON! CONGRATS!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("YOU WON! CONGRATS!")
    elif computer_choice == "paper":
        print("IT'S A TIE")
    elif computer_choice == "scissors":
        print("OH, THE COMPUTER WON...")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("OH, THE COMPUTER WON...")
    elif computer_choice == "paper":
        print("YOU WON! CONGRATS!")
    elif computer_choice == "scissors":
        print("IT'S A TIE")



# validate the input such that only if it is one of the expected values will we 
# ... continue with the rest of the program
# ... otherwise well stop the program before it tries to do anything else
# ... and well ask the user to run the program again




print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN")