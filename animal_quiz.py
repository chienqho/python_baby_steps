# Introduction message for the game
print("Guess the Animal")

# Set the number of chances the player has to answer each question
chances = 3

# Start a loop to allow the player multiple chances to answer the first question
while chances > 0:
    # Prompt the user to guess which bear lives at the North Pole
    question_1 = input("Which bear lives at the North Pole? ")

    # Check if the answer is correct
    if question_1.lower() == 'polar bear':
        # If correct, print a success message and break out of the loop
        print("Correct Answer")
        break
    else:
        # If incorrect, print a failure message and decrease the number of chances
        print("Sorry, wrong answer.")
        chances -= 1
        
        # Check if the player still has more chances
        if chances > 0:
            # If the player still has more chances, encourage them to try again
            print(f"You have {chances} chance(s) left. Try again.")
        else:
            # If the player has no more chances, end the game
            print("Sorry, you have run out of chances for question 1. Better luck next time!")

# Reset the number of chances for the next question
chances = 3

# Start a loop to allow the player multiple chances to answer the second question
while chances > 0:
    # Prompt the user to guess the fastest land animal
    question_2 = input("Which is the fastest land animal? ")

    # Check if the answer is correct
    if question_2.lower() == 'cheetah':
        # If correct, print a success message and break out of the loop
        print("Correct Answer")
        break
    else:
        # If incorrect, print a failure message and decrease the number of chances
        print("Sorry, wrong answer.")
        chances -= 1
        
        # Check if the player still has more chances
        if chances > 0:
            # If the player still has more chances, encourage them to try again
            print(f"You have {chances} chance(s) left. Try again.")
        else:
            # If the player has no more chances, end the game
            print("Sorry, you have run out of chances for question 2. Better luck next time!")

# Start a loop to allow the player multiple chances to answer the third question
while chances > 0:
    # Prompt the user to guess the largest animal
    question_3 = input("Which is the largest animal? ")

    # Check if the answer is correct
    if question_3.lower() == 'blue whale':
        # If correct, print a success message and break out of the loop
        print("Correct Answer")
        break
    else:
        # If incorrect, print a failure message and decrease the number of chances
        print("Sorry, wrong answer.")
        chances -= 1
        
        # Check if the player still has more chances
        if chances > 0:
            # If the player still has more chances, encourage them to try again
            print(f"You have {chances} chance(s) left. Try again.")
        else:
            # If the player has no more chances, end the game
            print("Sorry, you have run out of chances for question 3. Better luck next time!")
