# game.py

print("Rock, Paper, Scissors, Shoot!")


user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")

print("User Choice: ", user_choice)

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
exit()



# validate the input sch that only if it is one of the expected values will we 
# ... continue with the rest of the program
# ... otherwise well stop the program before it tries to do anything else
# ... and well ask the user to run the program again




print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN")