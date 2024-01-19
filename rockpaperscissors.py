import os

# ICD2O Final Project
# Charlie Pyke
# Rock Paper Scissors Program
# My project is a text version of Rock Paper Scissors. It will have two versions:
# 1. classic Rock-Paper-Scissors,
# 2. and the version from the Big Bang Theory, Rock-Paper-Scissors-Lizard-Spock.

# searched Google for this: https://www.geeksforgeeks.org/clear-screen-python/
# clear the screen so the game looks better
os.system("clear")

# Give the user my welcome prompts
print("Welcome to Charlie's Rock-Paper-Scissors Game!\n\n")
print("I can play two version of this game:\n")
print("1. Classic Rock-Paper-Scissors")
print("2. Rock-Paper-Scissors-Lizard-Spock\n")

# set the choice to nothing to start
game_choice = ""
# loop until the user gives us an acceptable input
while (game_choice != "1" and game_choice != "2" and game_choice != "quit"):
    # Ask the user what version they want to play
    game_choice = input("Which version of the game would you like to play? (1, 2, quit): ")

# Did the user want to quit?
if game_choice == "quit":
    print("\nThanks for playing!")
    exit()

# we have a game choice.
# set the instruction prompt to nothing to start
instructions_prompt = ""
while (instructions_prompt != "y" and instructions_prompt != "n"):
    # Ask the user if they want instructions
    instructions_prompt = input("\n\nWould you like to see the rules of the game? (y, n): ")

print(instructions_prompt)