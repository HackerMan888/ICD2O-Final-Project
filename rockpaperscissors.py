import os
import random

# ICD2O Final Project
# Charlie Pyke
# Rock Paper Scissors Program
# My project is a text version of Rock Paper Scissors. It will have two versions:
# 1. classic Rock-Paper-Scissors,
# 2. and the version from the Big Bang Theory, Rock-Paper-Scissors-Lizard-Spock.

# I used https://wrpsa.com/different-variations-of-rock-paper-scissors/ to help
# with game play. It says that you can use math to assign a value to each guess.
# The values are:
# 1 = rock
# 2 = paper
# 3 = scissors
# 4 = Spock
# 5 = lizard
# to figure out who wins, the value for player2's move is subtracted from the
# value of player1's move. The result of that is used for the python modulo
# function we learned about. The winner is calculated as:
# (player1 - player2) % (number of options [3 for classic and 5 for the Big Bang])
# if the result is an even number then player 2 wins
# if the result is an odd number then player 1 wins
# if the result is zero, then it's a tie

# searched Google for this: https://www.geeksforgeeks.org/clear-screen-python/
# clear the screen so the game looks better
os.system("clear")

# Give the user my welcome prompts
print("\n\nWelcome to Charlie's Rock-Paper-Scissors Game!\n\n")

# now ask for the player's name
# set the name to nothing to start
player_name = ""
# loop while they haven't entered anything
while player_name == "":
    player_name = input("\nWhat is your name? ")

print("\n\nWelcome", player_name)

# open the file to get the game statistics and display them
# do this later!

# set play_again to yes to start
play_again = "y"

# change game version - used later if the player keeps playing
change_version = "y"

# set the choice to nothing to start
game_choice = ""

while play_again == "y":
    play_again = ""

    if change_version == "y":
        # loop until the user gives us an acceptable input
        print("I can play two version of this game:\n")
        print("1. Classic Rock-Paper-Scissors")
        print("2. Rock-Paper-Scissors-Lizard-Spock\n")

        while game_choice != "1" and game_choice != "2" and game_choice != "quit":
            # Ask the user what version they want to play
            game_choice = input(
                "Which version of the game would you like to play? (1, 2, quit): "
            )
        change_version = ""

        # Did the user want to quit?
        if game_choice == "quit":
            print("\nThanks for playing", player_name)
            exit()

        # we have a game choice.
        # set the instruction prompt to nothing to start
        instructions_prompt = ""
        # loop while we don't have a valid input
        while instructions_prompt != "y" and instructions_prompt != "n":
            # Ask the user if they want instructions
            instructions_prompt = input(
                "\n\nWould you like to see the rules of the game? (y, n): "
            )

        # if the user wants instructions, give them the correct ones
        # instructions came from google: https://wrpsa.com/how-rps-rules-have-changed-over-time-an-evolution-in-strategy/
        # and https://wrpsa.com/different-variations-of-rock-paper-scissors/
        if instructions_prompt == "y":
            if game_choice == "1":
                print(
                    "\n\nEach player chooses one of three hand signs – rock, paper, or scissors."
                )
                print("Whichever hand sign beats the other wins the round.")
                print("Rock smashes scissors, scissors cuts paper, and paper covers rock.")
            elif game_choice == "2":
                print(
                    "\n\nEach player chooses one of five hand signs – rock, paper, scissors, lizard, Spock."
                )
                print("Whichever hand sign beats the other wins the round.")
                print(
                    "Like in classic, Rock smashes scissors, scissors cuts paper, and paper covers rock."
                )
                print(
                    "Also, Spock smashes scissors and vaporizes rock, but he is poisoned by a lizard and disproven by paper."
                )
                print(
                    "Lizard poisons Spock and eats paper but it is crushed by rock and decapitated by scissors."
                )

    # Game play!
    # define an array for the text of the valid moves
    valid_moves = ["rock", "paper", "scissors"]
    # define an array for number representing the valid moves. This is used
    # when we generate a random number to be the computer move
    valid_moves_numbers = [33, 66, 99]

    # if the user wants to play the Big Bang version, update the arrays
    if game_choice == "2":
        valid_moves = ["rock", "paper", "scissors", "Spock", "lizard"]
        valid_moves_numbers = [20, 40, 60, 80, 100]

    # set the winning_score to the same as a tie
    winning_score = 0

    # clear the screen so the game looks better
    os.system("clear")

    # Give the user my welcome prompts
    print("\n\nWelcome to Charlie's Rock-Paper-Scissors Game!\n\n")

    # Tell the player what input they are allowed to use
    print("\n\nReady", player_name, "\nYour valid move choices are: ", valid_moves, "\n")

    # loop while the score is a tie
    while winning_score == 0:
        # set player move to nothing
        player_move = ""

        # if the player didn't give a valid input, tell them and keep prompting
        while player_move not in valid_moves:
            player_move = input("Make your move: ")
            if player_move not in valid_moves:
                print("Please enter a valid move!\n")

        # tell the player their move
        print("\n\nYour move was:", player_move, "\n\n")
        # the value of the player move is the same as the index in the array plus 1
        player_move_value = valid_moves.index(player_move) + 1

        # generate the computer move
        # the maximum of the random number is the highest number from the value array we defined
        computer_move = random.randrange(1, valid_moves_numbers[len(valid_moves_numbers) - 1])
        if computer_move <= valid_moves_numbers[0]:
            # between 1 and the first value, so it's rock
            computer_move_text = "rock"
            computer_move_value = 1
        elif computer_move > valid_moves_numbers[0] and computer_move <= valid_moves_numbers[1]:
            # between the first and second values, so it's paper
            computer_move_text = "paper"
            computer_move_value = 2
        elif computer_move > valid_moves_numbers[1] and computer_move <= valid_moves_numbers[2]:
            # between the second and third values, so it's scissors
            computer_move_text = "scissors"
            computer_move_value = 3

        # if it's the Big Bang version, we have two more possible values
        if game_choice == "2":
            if (
                computer_move > valid_moves_numbers[2]
                and computer_move <= valid_moves_numbers[3]
            ):
                # if it's between the third and fourth value, it's lizard
                computer_move_text = "Spock"
                computer_move_value = 4
            elif (
                computer_move > valid_moves_numbers[3]
                and computer_move <= valid_moves_numbers[4]
            ):
                # this check could be just 'if greater than the value in [3]' but we used the
                # > [3] and <= [4] just to make sure
                computer_move_text = "lizard"
                computer_move_value = 5

        print("My move is", computer_move_text)
        # now do our calculation!
        winning_score = (player_move_value - computer_move_value) % len(valid_moves)

        if winning_score == 0:
            print("It's a tie!")

    if (winning_score % 2) == 0:
        print("\nI win!", computer_move_text, "beats", player_move)
    else:
        print("\nYou win!", player_move, "beats", computer_move_text)

    while play_again != "y" and play_again != "n":
        play_again = input("\n\nWould you like to keep playing? (y, n): ")
        if play_again == "y":
            while change_version != "y" and change_version != "n":
                change_version = input(
                    "Would you like to change game versions? (y, n): "
                    )

print("\n\nThanks for playing", player_name)

# write the scores file out. Do this later
