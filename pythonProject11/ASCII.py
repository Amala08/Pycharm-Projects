l_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z',]
u_alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W''X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
l_asc_value = 97
u_asc_value = 65
user_word = input("Enter any word: ")
key_shift = int(input("how many letter you would like to shift: "))
output = []
asc = " "
def asc(word,shift,l,u):
    for letter in word:
        if letter in l_alphabets:
            if letter == "a":
                spl = 123 - shift
                output.append(spl)
            else:
                position = l_alphabets.index(letter)
                new = position - shift
                result = l + new
                output.append(result)
        else:
            position = u_alphabets.index(letter)
            new = position + shift
            result = u + new
            output.append(result)
asc(user_word,key_shift,l_asc_value,u_asc_value)
print(f"The Encrypted ASCII code for the given word is {output}")










