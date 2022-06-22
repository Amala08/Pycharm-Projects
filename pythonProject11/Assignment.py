word = input("Enter any word: ")
word_list = list(word)
size = len(word)
replace_letter = input("Enter the letter to be replaced: ")
replace_place = int(input("Enter the position to be replaced with given letter: "))
output = []
def newword(word,char,place):
    for n in range(size):
        if n == place:
            output.append(char)
        else:
            output.append(word[n])
newword(word,replace_letter,replace_place)
word1 = " "
for letter in output:
    word1 += letter
print(f"The replaced word is {word1}")