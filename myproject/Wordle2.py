import wrevision
import random
words = wrevision.word_list
choose_word = random.choice(words)
choose_word_list = list(choose_word)
answers = []
for letters in choose_word:
    answers.append("_")
count = 0
while count < 6:
    guess_word = input("Enter any 5 letter word: ")
    guess_wordlist = list(guess_word)
    print(guess_wordlist)
    if guess_word == choose_word:
        print(f"Congrats!!! You Win")
        break
    else:
        for n in range(5):
            if guess_wordlist[n] == choose_word_list[n]:
                print(f"{guess_wordlist[n]} is in same place")
                answers.append(guess_word[n])
            elif guess_wordlist[n] == choose_word_list[n-1]:
                print(f"{guess_wordlist[n]} is in different place")
            elif guess_wordlist[n] == choose_word_list[n - 2]:
                print(f"{guess_wordlist[n]} is in different place")
            elif guess_wordlist[n] == choose_word_list[n-3]:
                print(f"{guess_wordlist[n]} is in different place")
            elif guess_wordlist[n] == choose_word_list[n-4]:
                print(f"{guess_wordlist[n]} is in different place")
            else:
                print(f"{guess_wordlist[n]} is not in chosen word")
    count = count + 1
else:
    print(f"You lose. The correct word is {choose_word}")

