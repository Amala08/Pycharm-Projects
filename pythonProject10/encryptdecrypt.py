alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
def encrypt(message, shift):
    encrypt_message = ""
    for letter in message: #zebra, 3
        position = alphabet.index(letter)
        new_position = position + shift
        encrypt_message += alphabet[new_position]
    return encrypt_message
def decrypt(message, shift):
    decrypt_message = ""
    for letter in message:
        position = alphabet.index(letter)
        new_position = position - shift
        decrypt_message += alphabet[new_position]
    return decrypt_message