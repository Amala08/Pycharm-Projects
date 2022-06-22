choose = input("E for Encrypt and D for Decrypt: ")
if choose == "E":
    atm_number = (input("Enter your 16 digits ATM number: "))
    size = len(atm_number)
    print(size)
    while True:
        if size < 16:
            atm_number = input("Enter your 16 digits ATM number: ")
            continue
        elif size > 16:
            atm_number = input("Enter your 16 digits ATM number: ")
            continue
        else:
            if size == 16:
                atm_pin = input("Enter your 4 digit pin number: ")
                encrypt = atm.encrypt(atm_number, atm_pin)
                # print(encrypt["pin number"])
                print(f"Your Secret pin is {encrypt['pin number']}")
                break


    #encrypt = atm.encrypt(atm_number,atm_pin)
    #print(encrypt["pin number"])