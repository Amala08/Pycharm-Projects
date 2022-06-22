#To find the factorial of given num
num = int(input("Enter any number: "))
fact = 1
print(f"The factorial of given number {num} is")
while num > 0:
    fact *= num
    num -= 1
print(fact)


