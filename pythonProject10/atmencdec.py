import atm
choose = input("E for Encrypt and D for Decrypt: ")
if choose == "E":
    atm_number = (input("Enter your 16 digits ATM number: "))
    atm_pin = input("Enter your 4 digit pin number: ")
    encrypt = atm.encrypt(atm_number,atm_pin)
    #print(encrypt["pin number"])
    print(f"Your Secret pin is {encrypt['pin number']}")
if choose == "D":
    atm_num_alpha = input("Enter number in alphabets to decrypt: ")
    atm_pin_alpha = input("Enter pin in alphabets to decrypt: ")
    decrypt = atm.decrypt(atm_num_alpha,atm_pin_alpha)
    print(f"Your atm pin is {decrypt}")


