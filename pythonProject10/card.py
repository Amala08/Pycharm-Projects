alphabets = {0: "X",1: "R",2: "Z",3: "T",4: "I",5: "N",6: "F",7: "O",8: "V",9: "K"}
def encrypt(number,pin):
    result = ""
    result1 = ""
    secret_number = {}
    for n in number:
        a = alphabets(int[n])
        result += a
    secret_number["card number"] = result
    for n in pin:
        b = alphabets[n]
        result1 += b
    secret_number["pin number"] = result1
    return secret_number