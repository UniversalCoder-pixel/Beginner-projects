import random

exit = False
user_points = 0
computer_points = 0

while not exit:
    options = ["rock", "paper", "scissors"]  # Fixed typo: "schssors" → "scissors"
    user_input = input("Choose rock, paper, scissors or exit: ").lower()  # Added .lower() for case-insensitivity
    
    if user_input == "exit":
        print("Game ended")
        print(f"You won a total score of {user_points} and the computer total score is {computer_points}")  # Fixed typo: "ottal" → "total"
        exit = True
        continue  # Skip the rest of the loop
    
    # Check for invalid input
    if user_input not in options:  # Fixed logic: was using OR which always evaluated to True
        print("Invalid input")
        continue  # Skip to next iteration
    
    computer_input = random.choice(options)
    
    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It is a tie!")
        elif computer_input == "paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("Computer wins")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your input is rock")
            print("Computer input is scissors")
            print("You win")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("You win")
            user_points += 1
        elif computer_input == "paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("It is a tie!")
        elif computer_input == "scissors":
            print("Your input is paper")
            print("Computer input is scissors")
            print("Computer wins")
            computer_points += 1

    elif user_input == "scissors":
        if computer_input == "rock":
            print("Your input is scissors")
            print("Computer input is rock")
            print("Computer wins")
            computer_points += 1
        elif computer_input == "paper":
            print("Your input is scissors")
            print("Computer input is paper")
            print("You win")
            user_points += 1  # Fixed: removed extra "computer_points += 1"
        elif computer_input == "scissors":
            print("Your input is scissors")
            print("Computer input is scissors")
            print("It is a tie!")
    
    print(f"\nScore - You: {user_points} | Computer: {computer_points}\n")  # Added score display after each round





