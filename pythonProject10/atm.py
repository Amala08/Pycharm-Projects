alphabets = {"0": "X","1": "R","2": "Z","3": "T","4": "I","5": "N","6": "F","7": "O","8": "V","9": "K"}
def encrypt(number,pin):
    result = ""
    result1 = ""
    secret_number = {}
    for n in number:
        a = alphabets[n]
        result += a
    secret_number["card number"] = result
    for n in pin:
        b = alphabets[n]
        result1 += b
    secret_number["pin number"] = result1
    return secret_number
def decrypt(number, pin):
    result2 = ""
    result3 = ""
    keys = list(alphabets.keys())
    values = list(alphabets.values())
    for n in number:
        a = keys[values.index(n)]
        result2 += a
    print(f"Your ATM number is {result2}")
    for n in pin:
        b = keys[values.index(n)]
        result3 += b
    return result3

