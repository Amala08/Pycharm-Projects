import random
words = ["apple", "paste", "listen", "blackmail", "psycho", "yesterday", "loan"]
choose_word = random.choice(words)
list1 = []
size = len(choose_word)
i = 0
word = ""
for letters in choose_word:
    list1.append("_")
print(f"The chosen word: {list1}")
while size > i:
    letter = input("Choose a letter: ")
    for position in range(size):
        if letter == choose_word[position]:
            list1[position] = letter
            print(list1)
            i = i - 1
    i = i + 1
for character in list1:
    word = word + character
if word == choose_word:
    print(f"You WON.The Word is {choose_word}")
else:
    print(f"You LOSE. The correct word is {choose_word}")