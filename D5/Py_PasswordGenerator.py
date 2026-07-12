# PASSWORD GENERATOR:-

import random


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


password=""
password_final=""

for i in range(1,lr+1):
    password+=random.choice(letters)

for i in range(1,sy+1):
    password+=random.choice(symbols)

for i in range(1,nr+1):
   password+=random.choice(numbers)

for i in range(0,len(password)):
   password_final+=random.choice(password)

print(f"Your password is: {password_final}")

# Another method to do it using Lists:-

password_list = []

for i in range(0, lr):
    password_list.append(random.choice(letters))

for i in range(0, sy):
    password_list.append(random.choice(symbols))

for i in range(0, nr):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password_new = "".join(password_list)

print(f"Your password is: {password_new}")