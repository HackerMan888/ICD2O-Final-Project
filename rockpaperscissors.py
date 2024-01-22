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

# store wins for this user
current_user_wins = 0

# open the file to get the game statistics and display them
# copy from the same work we did in Unit5-03
# https://sites.google.com/ocsb.ca/icd/units/unit-5/unit-5-03

# The file has:
# line 1 - total number of games played
# line 2 - number of computer wins
# line 3 - first high score name
# line 4 - number of wins for the player on the line before
# line 3 and 4 repear for the number of players we keep the score
# for. If there are not 5 high score, the file will only have names for
# the number of scores we have

# path.exists learned from Google:
# https://ioflood.com/blog/python-check-if-file-exists/

total_number_games = 0
total_number_wins = 0
high_score_position = -1
high_score_list = [["", 0], ["", 0], ["", 0], ["", 0], ["", 0]]

if os.path.exists("highscores.txt"):
    score_file = open("highscores.txt", "r")
    number_games_line = ""
    number_wins_line = ""
    high_score_line = ""

    # get the total number of games
    number_games_line = score_file.readline()
    if number_games_line != "":
        total_number_games = int(number_games_line.strip("\n"))

    # get the number of wins
    number_wins_line = score_file.readline()
    if number_wins_line != "":
        total_number_wins = int(number_wins_line.strip("\n"))

    print("\nSo far, I have played", total_number_games)
    print("and I have won", total_number_wins, "times.")

    high_score_line = score_file.readline()
    if high_score_line != "":
        high_score_position = 0
        print("\nThe top winners so far are:")

    while high_score_line != "":
        # store the name
        high_score_list[high_score_position][0] = high_score_line.strip("\n")
        # get the score for the name we just stored
        high_score_line = score_file.readline()
        # make sure we read something properly
        if high_score_line != "":
            # store the name's score
            high_score_list[high_score_position][1] = int(high_score_line.strip("\n"))
        else:
            high_score_list[high_score_position][1] = 0

        # format a line to print
        line_to_print = (
            str(high_score_position + 1)
            + ". "
            + str(high_score_list[high_score_position][0])
            + " with "
            + str(high_score_list[high_score_position][1])
            + " wins"
        )
        print(line_to_print)

        # move to the next name in the list
        high_score_position += 1
        # get the next line in the file, which should be a name
        high_score_line = score_file.readline()
    score_file.close()

# set play_again to yes to start
play_again = "y"

# change game version - used later if the player keeps playing
change_version = "y"

while play_again == "y":
    play_again = ""

    if change_version == "y":
        # set the choice to nothing to start
        game_choice = ""
        # loop until the user gives us an acceptable input
        print("\n\nI can play two version of this game:\n")
        print("1. Classic Rock-Paper-Scissors")
        print("2. Rock-Paper-Scissors-Lizard-Spock\n")

        while game_choice != "1" and game_choice != "2" and game_choice != "quit":
            # Ask the user what version they want to play
            game_choice = input(
                "Which version of the game would you like to play? (1, 2, quit): "
            )
        change_version = "y"

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
        # instructions came from google:
        # https://wrpsa.com/how-rps-rules-have-changed-over-time-an-evolution-in-strategy/
        # and https://wrpsa.com/different-variations-of-rock-paper-scissors/
        if instructions_prompt == "y":
            if game_choice == "1":
                print(
                    "\n\nEach player chooses one of three hand signs – rock, paper, or scissors."
                )
                print("Whichever hand sign beats the other wins the round.")
                print(
                    "Rock smashes scissors, scissors cuts paper, and paper covers rock."
                )
            elif game_choice == "2":
                print(
                    "\n\nEach player chooses one of five hand signs – rock, paper, scissors, lizard, Spock."
                )
                print(
                    "Whichever hand sign beats the other wins the round. Like in classic,"
                )
                print(
                    "rock smashes scissors, scissors cuts paper, and paper covers rock. Also, Spock smashes"
                )
                print(
                    "scissors and vaporizes rock, but he is poisoned by a lizard and disproven by paper."
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

    # clear the screen so the game looks better, but don't clear it if they asked for instructions
    if instructions_prompt != "y":
        os.system("clear")

        # Give the user my welcome prompts
        print("\n\nWelcome to Charlie's Rock-Paper-Scissors Game!\n\n")

    # Tell the player what input they are allowed to use
    print(
        "\n\nReady", player_name, "\nYour valid move choices are: ", valid_moves, "\n"
    )
    # increase the number of games played
    total_number_games += 1

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
        print("\n\nYour move was:", player_move)
        # the value of the player move is the same as the index in the array plus 1
        player_move_value = valid_moves.index(player_move) + 1

        # generate the computer move
        # the maximum of the random number is the highest number from the value array we defined
        computer_move = random.randrange(
            1, valid_moves_numbers[len(valid_moves_numbers) - 1]
        )
        if computer_move <= valid_moves_numbers[0]:
            # between 1 and the first value, so it's rock
            computer_move_text = "rock"
            computer_move_value = 1
        elif (
            computer_move > valid_moves_numbers[0]
            and computer_move <= valid_moves_numbers[1]
        ):
            # between the first and second values, so it's paper
            computer_move_text = "paper"
            computer_move_value = 2
        elif (
            computer_move > valid_moves_numbers[1]
            and computer_move <= valid_moves_numbers[2]
        ):
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
            print("It's a tie!\n")

    if (winning_score % 2) == 0:
        print("\nI win!", computer_move_text, "beats", player_move)
        # increase the number of computer wins
        total_number_wins += 1
    else:
        print("\nYou win!", player_move, "beats", computer_move_text)
        # increase the number of current user wins
        current_user_wins += 1

    while play_again != "y" and play_again != "n":
        play_again = input("\n\nWould you like to keep playing? (y, n): ")
        if play_again == "y":
            change_version = ""
            while change_version != "y" and change_version != "n":
                change_version = input(
                    "Would you like to change game versions? (y, n): "
                )

print("\n\nThanks for playing", player_name)

# save the high scores
score_file = open("highscores.txt", "w")
# save the file in the same structure we wanted to read
# The file has:
# line 1 - total number of games played
# line 2 - number of computer wins
# line 3 - first high score name
# line 4 - number of wins for the player on the line before
# line 3 and 4 repear for the number of players we keep the score
# for. If there are not 5 high score, the file will only have names for
# the number of scores we have

# write total number of games
score_file.write(str(total_number_games) + "\n")
# write total number of computer wins
score_file.write(str(total_number_wins) + "\n")

# update the user
print("\nNow, I have played", total_number_games)
print("and I have won", total_number_wins, "times.")

# update the highscores list

# Make sure the current user's score are added to the list
current_user_inserted = False
for list_position in range(0, 5):
    # does the current user match a score in the list?
    # Update their score in the old list before writing
    if high_score_list[list_position][0] == player_name:
        total_user_wins = high_score_list[list_position][1] + current_user_wins  # type: ignore[operator]
        # Update their score in the old list, just to make sure
        high_score_list[list_position][1] = total_user_wins
        current_user_inserted = True

# If we did'n update the current user's score, then
# insert the current player to the existing list
# This adds an extra object to our list. we'll fix that later
if not current_user_inserted:
    high_score_list.insert(high_score_position + 1, [player_name, current_user_wins])

# Now the current user's scores are updated or added to the list
# We need to create a new sorted list to output
new_high_score_list = ["", 0]

for old_list_position in range(0, 5):
    if len(new_high_score_list) == 0:
        if high_score_list[old_list_position][0] != "":
            new_high_score_list.insert(
                0,
                [
                    high_score_list[old_list_position][0],
                    high_score_list[old_list_position][1],
                ],
            )
    else:
        for new_list_position in range(0, len(new_high_score_list)):
            if (
                high_score_list[old_list_position][1]
                >= new_high_score_list[new_list_position][1]  # type: ignore[operator]
            ):
                if high_score_list[old_list_position][0] != "":
                    new_high_score_list.insert(
                        new_list_position,
                        [
                            high_score_list[old_list_position][0],
                            high_score_list[old_list_position][1],
                        ],
                    )
            else:
                # are we at the end of the new list?
                if new_list_position == (len(new_high_score_list) - 1):
                    if high_score_list[old_list_position][0] != "":
                        new_high_score_list.insert(
                            new_list_position + 1,
                            [
                                high_score_list[old_list_position][0],
                                high_score_list[old_list_position][1],
                            ],
                        )

# we should have a sorted list now
# write the list of high scores, and update if the current player is
# now in the list
output_position = 0
max_output_position = len(new_high_score_list) - 1
if max_output_position > 4:
    max_output_position = 4
print("\nThe top winners so far are:")
while output_position <= max_output_position:
    if new_high_score_list[output_position][0] != "":
        # format a line to print
        line_to_print = (
            str(output_position + 1)
            + ". "
            + str(new_high_score_list[output_position][0])
            + " with "
            + str(new_high_score_list[output_position][1])
            + " wins"
        )
        print(line_to_print)
        # write name to the file
        score_file.write(str(new_high_score_list[output_position][0]) + "\n")
        # write score to the file
        score_file.write(str(new_high_score_list[output_position][1]) + "\n")
    output_position += 1
score_file.close()
