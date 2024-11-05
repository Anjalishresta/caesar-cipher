# add your code here
def caesar_cipher(text, shift=5):
    encrypted_text = 

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            new_char = chr(((ord(char) - ascii_offset + shift) % 26) + ascii_offset)
            encrypted_text += new_char
        else:
            encrypted_text += char

    return encrypted_text

text_input = input(Please enter a sentence: )
encrypted_output = caesar_cipher(text_input)
print(The encrypted sentence is:, encrypted_output)
