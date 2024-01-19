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
while game_choice != "1" and game_choice != "2" and game_choice != "quit":
    # Ask the user what version they want to play
    game_choice = input("Which version of the game would you like to play? (1, 2, quit): ")

# Did the user want to quit?
if game_choice == "quit":
    print("\nThanks for playing!")
    exit()

# we have a game choice.
# set the instruction prompt to nothing to start
instructions_prompt = ""
# loop while we don't have a valid input
while instructions_prompt != "y" and instructions_prompt != "n":
    # Ask the user if they want instructions
    instructions_prompt = input("\n\nWould you like to see the rules of the game? (y, n): ")

# if the user wants instructions, give them the correct ones
# instructions came from google: https://wrpsa.com/how-rps-rules-have-changed-over-time-an-evolution-in-strategy/
# and https://wrpsa.com/different-variations-of-rock-paper-scissors/
if instructions_prompt == "y":
    if game_choice == "1":
        print(
            "\n\nEach player chooses one of three hand signs – rock, paper, or scissors."
            )
        print(
            "Whichever hand sign beats the other wins the round."
            )
        print(
            "Rock beats scissors, scissors cuts paper, and paper covers rock."
            )
    elif game_choice == "2":
        print(
            "\n\nEach player chooses one of five hand signs – rock, paper, scissors, lizard, Spock."
            )
        print(
            "Whichever hand sign beats the other wins the round."
            )
        print(
            "Link in classic, Rock beats scissors, scissors cuts paper, and paper covers rock."
            )
        print(
            "Also, Spock smashes scissors and vaporizes rock, but he is poisoned by a lizard and disproven by paper."
            )
        print(
            "Lizard poisons Spock and eats paper but it is crushed by rock and decapitated by scissors."
            )

# now ask for the player's name
# set the name to nothing to start
player_name = ""
# loop while they haven't entered anything
while player_name == "":
    player_name = input("\n\nWhat is your name? ")

print("\n\nWelcome", player_name)

# open the file to get the game statistics and display them
# do this later!
