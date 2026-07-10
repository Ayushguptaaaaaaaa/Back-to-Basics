import random

ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


User_choice=input("PLease enter your choice below:-\n1 for Rock\n2 for Paper\n3 for Scissors\n")

computer_choice=random.randint(1,3)

if User_choice=="1":
    print("You chose:-")
    print(ROCK)
elif User_choice=="2":
    print("You chose:-")
    print(PAPER)
elif User_choice=="3":
    print("You chose:-")
    print(SCISSORS)

if computer_choice==1:
    print("Computer chose:-")
    print(ROCK)
elif computer_choice==2:
    print("Computer chose:-")
    print(PAPER)
elif computer_choice==3:
    print("Computer chose:-")
    print(SCISSORS)


if int(User_choice)==computer_choice:
    print("It's a draw!")
elif User_choice=="1" and computer_choice==3:
    print("You win!")
elif User_choice=="2" and computer_choice==1:
    print("You win!")
elif User_choice=="3" and computer_choice==2:
    print("You win!")
else:
    print("You lose!")