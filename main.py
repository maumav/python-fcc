import random

def get_choices():
    player_choice = input("Enter a choice: ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

choices = get_choices()
print(choices)



def check_win(player, computer):
    print(f"You chose  {player}, computer chose  {computer} ")
    if player == computer:
        return ("It's a tie.")
    elif player == "rock":
        if computer == "scissors":
            return ("rock smashes scissors!")
    else:
        return "paper covers rock!"
    

check_win("rock", "paper")

