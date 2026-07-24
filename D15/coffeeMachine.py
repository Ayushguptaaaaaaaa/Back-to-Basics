LOGO = r"""
        ( (
         ) )
      ........
      |      |]   ~~~ COFFEE MACHINE ~~~
      \      /
       `----'
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def is_resource_sufficient(order_ingredients):
    """Requirement 4 — return True only if every ingredient is in stock."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Requirement 5 — sum the coins into a dollar total."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Requirement 6 — check payment, give change, bank the profit."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        resources["money"] += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    

def make_coffee(drink_name, order_ingredients):
    """Requirement 7 — deduct ingredients and serve the drink."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


print(LOGO)

is_on=True

while is_on:
    choice=input("Choose your drink: espresso/latte/cappuccino: ").lower()

    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif choice in MENU:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])



