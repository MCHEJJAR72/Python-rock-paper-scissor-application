Steps to Implement the Game
Import Required Modules:

You'll need the random module to allow the computer to make random choices.
Define Game Rules:

Define the rules for who wins based on the choices of the player and the computer.
Game Loop:

Continuously ask the player for input until they decide to quit.
Random Selection for Computer:

Use random.randint to let the computer randomly choose between "Rock", "Paper", or "Scissors".
Compare Choices:

Compare the player's choice and the computer's choice to determine the outcome of each round.
End Game:

When the player decides to quit (by entering "I quit"), display a farewell message.
Example Python Code
Here’s how you can implement this in Python:

import random

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Game Tied"
    elif (player_choice == "Rock" and computer_choice == "Paper") or \
         (player_choice == "Scissors" and computer_choice == "Rock") or \
         (player_choice == "Paper" and computer_choice == "Scissors"):
        return "You lose"
    else:
        return "You win"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        player_choice = input("Enter your choice (Rock/Paper/Scissors) or 'I quit' to end: ").strip().capitalize()
        
        if player_choice == "I quit":
            print("Thank you for playing!")
            break
        
        if player_choice not in ["Rock", "Paper", "Scissors"]:
            print("Invalid choice. Please enter Rock, Paper, or Scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chooses: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
Explanation:
get_computer_choice(): This function uses random.choice to randomly select one of the options ("Rock", "Paper", "Scissors") for the computer.

determine_winner(player_choice, computer_choice): This function checks the combinations of choices to determine the winner or if the game is tied.

main(): This is where the main game loop resides. It continuously asks the player for input until they decide to quit by entering "I quit". It validates the player's input, computes the computer's choice, determines the outcome of each round, and prints the result.

How to Run:
Copy the provided Python code into a .py file.
Run the file using a Python interpreter (python your_file.py).
Follow the prompts to play the game.