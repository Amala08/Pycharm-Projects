import wrevision
import random
print("  Word Scramble ")
print("*****************")
word = random.choice(wrevision.word_list)
word_list = list(word)
random.shuffle(word_list)
print(word_list)
output = input("Guess the correct word: ")
if word == output:
    print("Congrats!!!! You have guessed the correct word")
else:
    print(f"Incorrect.. The correct word is {word}")