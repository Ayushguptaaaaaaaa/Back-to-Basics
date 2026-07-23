import random

logo = """
    __  ___       __              
   / / / (_)___ _/ /_  ___  _____ 
  / /_/ / / __ `/ __ \\/ _ \\/ ___/ 
 / __  / / /_/ / / / /  __/ /     
/_/ /_/_/\\__, /_/ /_/\\___/_/      
     _  /____/    __                 
    / /  ____ _      _____  _____
   / /  / __ \\ | /| / / _ \\/ ___/
  / /__/ /_/ / |/ |/ /  __/ /    
 /_____\\____/|__/|__/\\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____/  
"""





data = [
    {'name': 'Instagram', 'follower_count': 346, 'description': 'Social media platform', 'country': 'United States'},
    {'name': 'Cristiano Ronaldo', 'follower_count': 215, 'description': 'Footballer', 'country': 'Portugal'},
    {'name': 'Ariana Grande', 'follower_count': 183, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Dwayne Johnson', 'follower_count': 181, 'description': 'Actor and wrestler', 'country': 'United States'},
    {'name': 'Selena Gomez', 'follower_count': 174, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Kylie Jenner', 'follower_count': 172, 'description': 'Reality TV personality', 'country': 'United States'},
    {'name': 'Kim Kardashian', 'follower_count': 167, 'description': 'Reality TV personality', 'country': 'United States'},
    {'name': 'Lionel Messi', 'follower_count': 149, 'description': 'Footballer', 'country': 'Argentina'},
    {'name': 'Beyonce', 'follower_count': 145, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Neymar', 'follower_count': 138, 'description': 'Footballer', 'country': 'Brazil'},
    {'name': 'National Geographic', 'follower_count': 135, 'description': 'Magazine', 'country': 'United States'},
    {'name': 'Justin Bieber', 'follower_count': 133, 'description': 'Musician', 'country': 'Canada'},
    {'name': 'Taylor Swift', 'follower_count': 131, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Kendall Jenner', 'follower_count': 127, 'description': 'Reality TV personality', 'country': 'United States'},
    {'name': 'Jennifer Lopez', 'follower_count': 119, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Nike', 'follower_count': 117, 'description': 'Sportswear multinational', 'country': 'United States'},
    {'name': 'Nicki Minaj', 'follower_count': 113, 'description': 'Musician', 'country': 'Trinidad and Tobago'},
    {'name': 'Khloe Kardashian', 'follower_count': 112, 'description': 'Reality TV personality', 'country': 'United States'},
    {'name': 'Miley Cyrus', 'follower_count': 108, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Katy Perry', 'follower_count': 104, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Kourtney Kardashian', 'follower_count': 102, 'description': 'Reality TV personality', 'country': 'United States'},
    {'name': 'Kevin Hart', 'follower_count': 89, 'description': 'Comedian and actor', 'country': 'United States'},
    {'name': 'Ellen DeGeneres', 'follower_count': 87, 'description': 'Comedian and TV host', 'country': 'United States'},
]

def format_data(account):
    name=account['name']
    description=account['description']
    country=account['country']
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers,b_followers):
    if a_followers>b_followers:
        return guess=="a"
    else:
        return guess=="b"
    
def game():
    print(logo)
    score=0
    game_should_continue=True
    account_b=random.choice(data)

    while game_should_continue:
        account_a=account_b
        account_b=random.choice(data)

        while account_a==account_b:
            account_b=random.choice(data)

        print(f"Compare A: {format_data(account_a)}")
        print("vs")
        print(f"Against B: {format_data(account_b)}")

        guess=input("Who has more Followers? Type A or B: ").lower()

        a_follower_count=account_a["follower_count"]
        b_follower_count=account_b["follower_count"]
        is_correct=check_answer(guess,a_follower_count,b_follower_count)

        print("\n"*20)
        print(logo)

        if is_correct:
            score+=1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False

game() 