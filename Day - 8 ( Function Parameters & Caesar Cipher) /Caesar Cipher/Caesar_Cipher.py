from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Encrypting The message
def caesar(plain_text, shift_amount, process):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if process == "encode":
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        elif process == "decode":
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    print(f"The {process}d, string is: {cipher_text}.")

caesar(plain_text=text,shift_amount=shift,process=direction)

# A simple Caesar Cipher program, using for loops and logical operations in python. 
