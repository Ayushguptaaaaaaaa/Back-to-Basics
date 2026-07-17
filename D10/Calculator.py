logo = r'''
                 _____________________
                |  _________________  |
                | |              0. | |
                | |_________________| |
                |  ___ ___ ___   ___  |
                | | 7 | 8 | 9 | | + | |
                | |___|___|___| |___| |
                | | 4 | 5 | 6 | | - | |
                | |___|___|___| |___| |
                | | 1 | 2 | 3 | | x | |
                | |___|___|___| |___| |
                | | . | 0 | = | | / | |
                | |___|___|___| |___| |
                |_____________________|

   ____      _            _       _
  / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __
 | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |__| (_| | | (__| |_| | | (_| | || (_) | |
  \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
'''
print(logo)


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


def calculator(num1, Op, num2):
    if Op== "+":
        result=add(num1,num2)
        print(result)
    elif Op== "-":
        result=subtract(num1,num2)
        print(result)
    elif Op== "*":
        result=multiply(num1,num2)
        print(result)
    elif Op== "/":
        result=divide(num1,num2)
        print(result)


continue_or_not=True

while(continue_or_not==True):
    num1=int(input("Enter first Number: "))
    print("+"," -"," *"," /")
    Op=input("Enter Operation: ")
    num2=int(input("Enter second Number: "))

    calculator(num1, Op, num2)

    restart=input("Do u want to continue: 'y' or 'n': ")
    if restart=='n':
        continue_or_not=False


