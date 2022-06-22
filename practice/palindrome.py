string_1 = input("Enter any word: ")
string_2 = string_1[: : -1]
if string_1 == string_2:
    print("Palindrome")
else:
    print("Not a Palindrome")

