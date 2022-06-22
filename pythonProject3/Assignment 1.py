#Find given num is odd or even using if method
num = int(input("Enter any number: "))
if num % 2 == 0:
    print(f"The given num '{num}' is 'Even'")
else:
    print(f"The given num '{num}' is 'Odd'")

#Find given num is odd or even using boolean method
num = int(input("Enter any number: "))
print(f"The given num {num} is Even" * (num % 2 == 0),f"The given num {num} is Odd" * (num % 2 != 0))
