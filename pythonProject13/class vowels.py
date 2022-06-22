class Vowels:

    def __init__(self):
        self.word = input("Enter any word/sentence: ").lower()
        self.vowels = "aeiou"

    def count_vowel_character(self):
        count = 0
        for i in self.word:
            for j in self.vowels:
                if i == j:
                    count += 1
        return count

count = Vowels()
print(f"Total Vowels in given word or sentence is {count.count_vowel_character()}")