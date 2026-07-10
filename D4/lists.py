# states_in_us=["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

# print(states_in_us)
# print(states_in_us[0])
# print(states_in_us[-1])
# print(states_in_us[0])
# print(states_in_us[0:3])

# states_in_us[0]="Ayushland"
# states_in_us.append("Bittuland")
# print(states_in_us)



# WHO WILL PAY THE BILL?

import random

names = ["Alice", "Bob", "Charlie", "David", "Eve"]

random_choice=random.randint(0, len(names)-1)
print(names[random_choice] + " is going to pay the bill today!")

# OR

print(f"{random.choice(names)} is going to pay the bill today!")



# INDEX OUT OF RANGE ERROR:-

# This error occurs when you try to access an index that doesn't exist in the list.
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits=["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables=["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]