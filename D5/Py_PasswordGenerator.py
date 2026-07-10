# PASSWORD GENERATOR:-

import random

# The characters we can pick from
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")

lr=int(input("How many letters do you want in your password? "))
sy=int(input("How many symbols do you want in your password? "))
nr=int(input("How many numbers do you want in your password? "))

password=[]
password_final=""

for i in range(1,lr+1):
    password.append(random.choice(letters))

for i in range(1,sy+1):
    password.append(random.choice(symbols))

for i in range(1,nr+1):
    password.append(random.choice(numbers))

password_final=password_final.join(password)

print(f"Your password is: {password_final}")