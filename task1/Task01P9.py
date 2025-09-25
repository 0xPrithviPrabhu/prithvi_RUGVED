#python function to encrypt a string using Ceasar’s Cipher
def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():  # Check if character is an alphabet
            shift_base = ord('A') if char.isupper() else ord('a')
            # Perform the shift
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabet characters are added unchanged
    
    return encrypted_text
# Example usage
input_string = input("Enter a string to encrypt: ")
shift_value = int(input("Enter the shift value (positive integer): "))
if shift_value < 0:
    print("Shift value should be a positive integer.")
else:
    encrypted_string = caesar_cipher_encrypt(input_string, shift_value)
    print("Original string:", input_string)
    print("Encrypted string:", encrypted_string)
