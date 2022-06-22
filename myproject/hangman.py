import random
import revision
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   

            '''
words = revision.word_list
choose_word = random.choice(words)
list1 = []
size = len(choose_word)
i = 0
j = -1
for letters in choose_word:
    list1.append("_")
print(f"The Puzzle word: {list1}")
while size > i:

    letter = input("Guess a letter: ")
    for position in range(size):
        if letter == choose_word[position]:
            list1[position] = letter
            print(list1)
            i = i - 1
    if list1.count(letter) <= 0:
        print(stages[j])
        print(list1)
        j = j - 1
        if j == -8:
            print(logo)
            print(f"You LOSE. The correct word is {choose_word}")
            break
    guess_word = input("Do you want to Guess the word. If Yes enter Y and No enter N: ")
    if guess_word == "Y":
        guessed_word = input("Enter the word: ")
        if guessed_word == choose_word:
            print("Congrats!!! You Win")
            break
    else:
        continue
    if list1.count("-") <= 0:
        print("Congrats!!! You Win")
        break
    i = i + 1
