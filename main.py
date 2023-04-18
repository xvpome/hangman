alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
state = True
action = 0
answer = ""
def decrypt(textorino, shiftAmmount):
    dec_text = ""
    for letter in textorino:
        position = alphabet.index(letter)
        new_position = position - shiftAmmount
        if new_position < 0:
            new_position = position + shiftAmmount
        new_letter = alphabet[new_position]
        dec_text += new_letter
    print(dec_text)
def encrypt(textorino, shiftammount):
    encText = ""
    for letter in textorino:
        position = alphabet.index(letter)
        new_position = position + shiftammount
        if new_position > len(alphabet):
            new_position = position - shiftammount
        newletter = alphabet[new_position]
        encText += newletter
    print(encText)
while state:
    direction = input("Do you want to encrypt or decrypt: ")
    text = input("Enter your message: ")
    shift = int(input("Type the shift number: "))

    if direction.lower() == "encrypt":
        encrypt(text, shift)
        action = 1
    elif direction.lower() == "decrypt":
        encrypt(text, shift)
        action = 1
    if action == 1:
        answer = input("Type yes if you want to go again. no if not\n")
    if answer.lower() == "no":
        break
