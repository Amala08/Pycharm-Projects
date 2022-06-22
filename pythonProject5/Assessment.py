numbers = []
for number in range(51,501):
    numbers.append(number)#Adding the number from range to the list
print(f"numbers = {numbers}")
fives = []
for num in numbers:
    if num % 5 == 0: #Using if statement to check the number is divisible by 5
        fives.append(num)#if statement ended true then those numbers are added to the list
print(f"List of numbers divisible by five = {fives}")
# To find the length of the list
print(f"The Length of the number list is {len(numbers)}")
print(f"The Length of the five divisible list is {len(fives)}")

