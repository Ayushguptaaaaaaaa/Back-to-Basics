print("Hello"[0])
print("Hello"[4])
print("Hello"[-1]) #This is same as the above line

print("123" + "345") #This is concatenation of two strings not addition of two numbers

print(123 + 345) #This is addition of two numbers not concatenation of two strings

print(3.2234) #This is a float number


#TYPE OF DATATYPES(primitive datatypes):-
print(type(3.2234)) #This will show the Float type of the variable
print(type("Hello")) #This will show the String type of the variable
print(type(123)) #This will show the Integer type of the variable
print(type(True)) #This will show the Boolean type of the variable

#Type conversion:-
print(int("123")+int("345")) #This will convert the string into integer and then add them

# print("Number of letters in your name: "+ str(len(input("What is your name? ")))) #This will take the input from user and then count the number of letters in the name and then print it


#MATHEMATICAL OPERATORS:-
print(3 + 5) #Addition
print(7 - 4) #Subtraction
print(3 * 2) #Multiplication
print(6 / 2) #Division (This will always result in a float)
print(2 ** 3) #Exponentiation(2 raised to the power of 3)
print(5 % 2) #Modulus (This will give the remainder)
print(5 // 2) #Floor Division (This will give the quotient without the remainder)

print(3 * 3 + 3 / 3 - 3) #This will follow the PEMDAS rule and give the result


#ROUNDING NUMBERS:-
print(round(8/3, 2)) #This will round the number to 2 decimal places

#ASSIGNMENT OPERATORS:-
score = 0
score += 1 #This is same as score = score + 1
score -= 1 #This is same as score = score - 1

height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}") #This is called f-string which will print the value of the variable in the string

