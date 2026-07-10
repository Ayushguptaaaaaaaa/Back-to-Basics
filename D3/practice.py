# #IF-ELSE STATEMENT:-

# print("Welcome to the RollerCoaster!")

# height=int(input("What is your height in cm? "))

# if height>=120:
#     print("You can ride the rollercoaster!")
# else: 
#     print(f"Sorry, you have to grow taller by {120-height}cm before you can ride.")


# MODULO OPERATOR:-
# The modulo operator (%) returns the remainder of a division operation.

#Challenge: Write a program that works out whether if a given number is an odd or even number.
# num=int(input("Enter a Number: "))
# if num%2==0:
#     print(f"{num} is an Even Number.")
# else:
#     print(f"{num} is an Odd Number.")



# NESTED IF-ELSE STATEMENT:-
# height=int(input("What is your height in cm? "))

# if(height>=120):
#     age=int(input("You can ride the rollercoaster but confirm your age first: "))
#     if age>18:
#         print("You are eligible to ride, kindly pay 12$ for the ride.")
#     elif(age >=12 and age<=18):
#         print("You are eligible to ride, kindly pay 7$ for the ride.")
#     elif(age < 12):
#         print("You are eligible to ride, kindly pay 5$ for the ride.")
# else:
#     print(f"Sorry, you have to grow taller by {120-height}cm before you can ride.")


# if(height>=120):
#     age=int(input("You can ride the rollercoaster but confirm your age first: "))
#     bill=0
#     if age>18:
#         bill=12
#     elif(age >=12 and age<=18):
#         bill=7
#     elif(age < 12):
#         bill=5
#     wants_photo=input("Do you want a photo taken? Y or N: ")
#     if wants_photo=="Y":
#         bill+=3
#     print(f"Your final bill is ${bill}.")
# else:
#     print(f"Sorry, you have to grow taller by {120-height}cm before you can ride.")


# CHALLENEGE- PYTHON PIZZA:-

# p_size=input("What size pizza do you want? S, M, or L: ")
# pep=input("Do you want pepperoni? Y or N: ")
# extra_cheese=input("Do you want extra cheese? Y or N: ")
# bill=0

# if(p_size=="S"):
#     bill+=15
#     if(pep=="Y"):
#         bill+=2
#     if(extra_cheese=="Y"):
#         bill+=1
# elif(p_size=="M"):
#     bill+=20
#     if(pep=="Y"):
#         bill+=3
#     if(extra_cheese=="Y"):
#         bill+=1
# elif(p_size=="L"):
#     bill+=25
#     if(pep=='Y'):
#         bill+=3
#     if(extra_cheese=='Y'):
#         bill+=1
# else:
#     print("Invalid Input.")
#     exit()

# print(f"Your final bill is ${bill}.")


# LOGICAL OPERATORS:-
# Logical operators are used to combine conditional statements.
# and, or, not are the logical operators in Python.

# true and true = true
# true and false = false
# false and true = false
# false and false = false

# true or true = true
# true or false = true
# false or true = true
# false or false = false

# not true = false
# not false = true


# height=int(input("What is your height in cm? "))

# if(height>=120):
#     age=int(input("You can ride the rollercoaster but confirm your age first: "))
#     bill=0
#     if (age>=45 and age<=55):
#         bill=0
#     elif age>18:
#         bill=12
#     elif(age >=12 and age<=18):
#         bill=7
#     elif(age < 12):
#         bill=5
#     wants_photo=input("Do you want a photo taken? Y or N: ")
#     if wants_photo=="Y":
#         bill+=3
#     print(f"Your final bill is ${bill}.")
# else:
#     print(f"Sorry, you have to grow taller by {120-height}cm before you can ride.")



