import os

# ICD2O Final Project
# Charlie Pyke
# Rock Paper Scissors Program
# My project is a text version of Rock Paper Scissors. It will have two versions: 
# 1. classic Rock-Paper-Scissors, 
# 2. and the version from the Big Bang Theory, Rock-Paper-Scissors-Lizard-Spock.

# searched Google for this: https://www.geeksforgeeks.org/clear-screen-python/
# clear the screen so the game looks better
os.system('clear')

# Give the user my welcome prompts
print('Welcome to Charlie\'s Rock-Paper-Scissors Game!\n\n')
print('I can play two version of this game:\n')
print('1. Classic Rock-Paper-Scissors')
print('2. Rock-Paper-Scissors-Lizard-Spock\n')

# Ask the user what version they want to play
game_choice = input('Which version of the game would you like to play? (1, 2, quit): ')