import random

stages = [
    # Stage 0 — full figure (game over)
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========""",

    # Stage 1 — both arms
    """
     +---+ 
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",

    # Stage 2 — one arm
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",

    # Stage 3 — head + torso
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",

    # Stage 4 — head
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",

    # Stage 5 — empty gallows
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
]


word_list = ["aardvark", "baboon", "camel"]

lives = len(stages) - 1          # 5, so it always matches stage indices 0..5
word = random.choice(word_list)

placeholder = ""
for i in word:
    placeholder += "_"

print(placeholder)
print("\n")


gameover = False
correct_letters = []

while gameover == False:
    guess = input("Guess a Letter: ").lower()
    display = ""

    for i in word:
        if i == guess:
            display += i
            if guess not in correct_letters:      # only record it once
                correct_letters.append(guess)
        elif i in correct_letters:
            display += i
        else:
            display += "_",
    print(display)

    if guess not in word:
        lives -= 1
        if lives == 0:                            # only lose when out of lives
            gameover = True
            print(f"You Lose! The word was '{word}'.")

    if "_" not in display:                        # win check
        gameover = True
        print("You Win!")

    print(stages[lives])
