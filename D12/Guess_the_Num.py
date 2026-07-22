# Guess the Number:-
import random

logo = r"""
   ____                       _____ _
  / ___|_   _  ___  ___ ___  |_   _| |__   ___
 | |  _| | | |/ _ \/ __/ __|   | | | '_ \ / _ \
 | |_| | |_| |  __/\__ \__ \   | | | | | |  __/
  \____|\__,_|\___||___/___/   |_| |_| |_|\___|
  _   _                 _                _
 | \ | |_   _ _ __ ___ | |__   ___ _ __ | |
 |  \| | | | | '_ ` _ \| '_ \ / _ \ '__|| |
 | |\  | |_| | | | | | | |_) |  __/ |   |_|
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   (_)
"""
print(logo)



def game(computer_num, medium):
    if (medium == 'easy'):
        for i in range(10):
            guess=int(input("Make a Guess: "))
            if(guess==computer_num):
                print("You Guess is Correct. You Won!")
            elif(guess>computer_num):
                print("Too High")
                print(f"You have {10-(i+1)} guesses left")
            else:
                print("Too Low")
                print(f"You have {10-(i+1)} guesses left")

        print("You Lose!")


    elif (medium == 'hard'):
        for i in range(5):
            guess=int(input("Make a Guess: "))
            if(guess==computer_num):
                print("You Guess is Correct. You Won!")
            elif(guess>computer_num):
                print("Too High")
                print(f"You have {5-(i+1)} guesses left")
            else:
                print("Too Low")
                print(f"You have {5-(i+1)} guesses left")
        print("You Lose!")



print("I'm thinking a number from 1 to 100!\n")
print("Welcome to the Number Guessing Game!\n")

computer_num=random.choice(range(101))

print(f"The correct number is {computer_num}")

medium=input("Select the difficuty 'Easy' or 'Hard': ").lower()

game(computer_num, medium)



 