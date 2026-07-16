# DICTIONARIES IN PYTHON:-

# programming_dictioary={
#     "Bug": "An error in a program that causes it to behave in an unexpected or incorrect way.",
#     "function": "A named, reusable block of code that performs a specific task when called.",
#     "Loop": "A programming construct that repeats a block of code until a condition is met."
# }

# print(programming_dictioary["function"])
# print(programming_dictioary)

# empty_dict={}

# programming_dictioary={}
# print(programming_dictioary)

# programming_dictioary["Bug"]="A moth in your computer"

# for key in programming_dictioary:
#     print(key)
#     print(programming_dictioary[key])\


# NESTED LISTS AND DICTIONARIES:-

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }

# travel_Log= {
#     "France": ["Paris", "Little", "Dijomn"],
#     "Germany":["Stuttgart", "Berlin"]
# }

# Print Little:-

# print(travel_Log["France"][1])

# nested_list=["A", "B", {"C", "D"}]

# print(nested_list[2][1])


travel_Log= {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin", "Hamburg"],
        "total_visits": 5
    }
}

print(travel_Log["Germany"]["cities_visited"][0])


