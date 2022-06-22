num = int(input("Enter the number: "))
n = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",  8: "Eight", 9: "Nine"}
numbers = []
output = ""
while num > 0:
    num1 = num % 10
    num = num // 10
    numbers.append(num1)
reversed_list = numbers[::-1]
for number in reversed_list:
    word = n[number]
    output += word + " "
print(output)