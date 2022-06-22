num = int(input("Enter the number: "))
numbers = []
while num > 0:
    num1 = num % 10
    num = num // 10
    numbers.insert(0,num1)
size = len(numbers)
high_num = []
while size > 0:
    highest = numbers[0]
    for n in numbers:
        if n > highest:
            highest = n
    numbers.remove(highest)
    size = size-1
    high_num.append(highest)
max_number = ""
for high in high_num:
    max_number = max_number + str(high) + ""
max_num = int(max_number)
print(f"Highest number = {max_num}")
length = len(high_num)
low_num = []
while length > 0:
    lowest = high_num[0]
    for n in high_num:
        if n < lowest:
            lowest = n
    high_num.remove(lowest)
    length = length-1
    low_num.append(lowest)
min_number = ""
for low in low_num:
    min_number = min_number + str(low) + ""
min_num = int(min_number)
print(f"Lowest number = {min_num}")
Total = max_num - min_num
print(f"The Difference between {max_num} and {min_num} is {Total}")



