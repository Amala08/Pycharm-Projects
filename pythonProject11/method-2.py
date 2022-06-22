word = input("Enter any word: ")
word_list = list(word)
size = len(word)
replace_letter = input("Enter the letter to be replaced: ")
replace_place = int(input("Enter the position to be replaced with given letter: "))
def new_word(word,char,place):
    output = " "
    for n in range(size):
        if n == place:
            output += char
        else:
            output += word[n]
    print(f"The replaced word is{output}")
new_word(word,replace_letter,replace_place)
