# import random

# def get_choices():
#     player_choice = input("Enter a choice: ")
#     options = ["rock", "paper", "scissors"]
#     computer_choice = random.choice(options)
#     choices = {"player": player_choice, "computer": computer_choice}
#     return choices

# choices = get_choices()
# print(choices)



# def check_win(player, computer):
#     print(f"You chose  {player}, computer chose  {computer} ")
#     if player == computer:
#         return ("It's a tie.")
#     elif player == "rock":
#         if computer == "scissors":
#             return ("rock smashes scissors!")
#         else:
#             return ("Paper covers rock! You lose")  
#     elif player == "paper":
#         if computer == "rock":
#             return ("paper smashes rock! You win")
#         else:
#             return "Scissors cuts paper! You lose"
#     elif player == "scissors":
#         if computer == "paper":
#             return ("scissors smashes paper! You win")
#         else:
#             return ("Rock breaks scissors! You lose")

# choices = get_choices()

# result = check_win(choices["player"], choices["computer"])
# print(result)

#Asking for input from user.
# print("What is your age")
# age = input()
# print("Your age is " + age)

#Lists
# names = ['John', 'Kennedy', 'Marshe', 'Ken']
# names[2] = "Java" #change index 2 to Java.
# print(names) #names list will result in new updated list.
# # names.append
# names.extend(["Sara", "Jude"]) #add 2 new items to the list.
# names.remove("John")
# names[1:1] = ["Test1", "Test2"] #insert new items in the middle of list.
# names.append("jake")
# names.sort(key=str.lower) #sorts the items in alphabetical order.
# print(names)

#Tuples, uses parenthesis () instead of []

# name2 = "roger", "Syd"
# print(sorted(name2))

#Dictionaries
# dog = {"name": "Roger", "age": 8}
# print(dog.get("name"))

#Functions 

# def hello(name, age): #parameters here 
#     print("Hello " + name + " you are " + str(age) + " years old.")
# hello("Brad", 29) #arguments

# def hello(name):
#     print("Hello " + name + "!")
#     return name, "Beau", 8
# print(hello("Syd"))

# Functions variable scope
# age = 28 #global scope variable
# def test():
#     age2 = 29
#     print(age2)
# test()
#print(age2) #not available outside the function, = error.

#Objects 
# age = 8
# print(age.real)
# print(age.imag)
# print(age.bit_length())

# items = [1, 2]

#Loops: while and for
# condition = True
# while condition == True:
#     print("The condition is True.")
#     condition = False 

# count = 0
# while count < 10:
#     print("condition is true.")
#     count += 1

items = [1,2,3,4]
for item in items:
    print(item)   