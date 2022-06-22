import encryptdecrypt
choose = input("E for Encrypt and D for Decrypt: ")
if choose == "E":
    user_message = input("Enter the message you like to send: ")
    user_shift = int(input("How many letters you would like to shift: "))
    result = encryptdecrypt.encrypt(user_message,user_shift)
    print(f"The Encrypted message is {result}")
if choose == "D":
    user_message = input("Enter the message you like to decrypt: ")
    user_shift = int(input("How many letters you would like to shift: "))
    result = encryptdecrypt.decrypt(user_message,user_shift)
    print(f"The Decrypted message is {result}")