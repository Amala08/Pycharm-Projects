import wrevision
import random
words = wrevision.word_list
choose_word = random.choice(words)
choose_word_list = list(choose_word)
answer = []
for letters in choose_word:
    answer.append("_")
print(answer)
count = 0
while count < 6:
    guess_word = input("Enter any 5 letter word: ")
    guess_wordlist = list(guess_word)
    for letter in guess_wordlist:
        if letter == choose_word_list[0]:
            answer[0] = letter
        if letter == choose_word_list[1]:
            answer[1] = letter
        if letter == choose_word_list[2]:
            answer[2] = letter
        if letter == choose_word_list[3]:
            answer[3] = letter
        if letter == choose_word_list[4]:
            answer[4] = letter
    print(answer)
    if answer.count("_") == 0:
        print(f"Congrats!!! You Win")
        break
    count = count + 1
if choose_word_list != answer:
    print(f"You lose. The correct word is {choose_word}")
