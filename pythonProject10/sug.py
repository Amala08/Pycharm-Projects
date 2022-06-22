user_sentence = input("Enter your sentence : ")
words = user_sentence.split()
print(words)
def rev(statement):
    reversed_sentence = " "
    for word in statement:
        size = len(word)
        for n in reversed(range(size)):
            reversed_sentence += word[n] + " "
    print(reversed_sentence)
rev(words)