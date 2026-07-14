# FUNCTION WITH INPUT:-

# def greet(name):
#     print(f"Hello {name}")
#     print("How do you do?")
#     print("Isn't the weather nice?")

# greet("Ayush")
# greet("Sonu")


# def greet_with(name, location):
    # print(f"Hello {name}, How is the weather in {location}?")

# greet_with("Ayush","India")

# ---------OR-------

# greet_with(location="India",name="Ayush")


# CAESAR'S CYPHER:-
logo = '''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88

  ,ad8888ba,   88  88888888ba  88        88  88888888888  88888888ba
 d8"'    `"8b  88  88      "8b 88        88  88           88      "8b
d8'            88  88      ,8P 88        88  88           88      ,8P
88             88  88aaaaaa8P' 88aaaaaaaa88  88aaaaa      88aaaaaa8P'
88             88  88""""""'   88""""""""88  88"""""      88""""88'
Y8,            88  88          88        88  88           88    `8b
 Y8a.    .a8P  88  88          88        88  88           88     `8b
  `"Y8888Y"'   88  88          88        88  88888888888  88      `8b
'''



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caeser(original_text,shift_amount,encode_or_decode):
    cipher_text=""
    if encode_or_decode=="decode":
        shift_amount*=-1

    for letter in original_text:
        if letter not in alphabet:
            cipher_text+=letter
        else:
        
            shifted_position=alphabet.index(letter)+ shift_amount
            shifted_position%=len(alphabet)
            cipher_text+=alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {cipher_text}")




print(logo)
should_continue=True

while should_continue==True:
    direction=input("Type 'encode' to encrypt or 'decode to decrypt:")
    text=input("Type your message: ").lower()
    shift=int(input("Type your shift number: "))

    caeser(original_text=text, shift_amount=shift,encode_or_decode=direction)

    restart=input("Type 'yes' if you want to go again OR type 'no': ")

    if restart=='no':
       should_continue=False
       print("GoodBye!")