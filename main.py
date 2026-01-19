import random

def get_choices():
    player_choice = input("Enter a choice: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

choices = get_choices()
print(choices)

food = ["pizza", "cake", "eggs"]
dinner = random.choice(food)

def check_win(player, computer):
    return [player, computer]
