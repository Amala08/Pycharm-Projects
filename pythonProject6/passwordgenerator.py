import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
no_lettters = int(input("Enter number of letters in your password : "))
no_numbers = int(input("Enter number of numbers in your password : "))
no_symbols = int(input("Enter number of symbols in your password : "))
password = ""
password_list = []
for char in range(1,no_lettters + 1):
    password_list.append(random.choice(letters))
for num in range(1, no_numbers + 1):
    password_list.append(random.choice(numbers))
for symbol in range(1, no_symbols + 1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
print(f"password in list : {password_list}")
#to convert the list into string
for char in password_list:
    password = password + char

print(f"Your new password is {password}")





