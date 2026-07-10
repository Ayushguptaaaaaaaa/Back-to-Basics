player_name=input("Enter Player's name:\n")

print(f"Welcome {player_name} to the Treasure Island!\nYour mission is to find the treasure, This is perhaps the greatest Oppotunity life has Offered You.\nBut Eventually you will end your suffering by finding the trasure or by dying in the process.\n")

print("LETS BEGIN THE GAME!\n")


dir=input("You are at a cross road. Where do you want to go? Type 'left' or 'right':\n").lower()

if dir=="left":
    swim=input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across:\n").lower()
    if swim=="wait":
        door_colour=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if door_colour=="red":
            print("You enter a room full of fire. Game Over. YOU DIED!\n")
        elif(door_colour=="blue"):
            print("You enter a room full of Grizzly Bears. Game Over. YOU DIED!\n")
        elif(door_colour=="yellow"):
            print("Congratulations! You found the treasure! You Won fotune for Life, You are now richer than the Richest Empires this World has Ever seen. From today you will be remembered as the greatest adventurer this world has ever known.\n")
        else:
            print("You chose a door that doesn't exist. You Cheated! Game Over. YOU SHALL ROT IN HELL FOR YOUR DECEPTION!\n")
    else:
        print("You get attacked by an angry trout. Game Over. YOU DIED!\n")
else:
    print("You fell into a hole. Game Over. YOU DIED!\n")
