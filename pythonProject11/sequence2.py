num1 = input("Enter a list of numbers: ")
num2 = input("Enter a list of numbers: ")
num1_list = num1.split(",")
num2_list = num2.split(",")
for n in range(len(num1_list)):
    num1_list[n] = int(num1_list[n])
for n in range(len(num2_list)):
    num2_list[n] = int(num2_list[n])
#def is_consecutive_sequence(number1,number2):
    number = num1_list + num2_list
    numbers = []
    asc_numbers = []
    for n in number:
        if n not in numbers:
            numbers.append(n)
    print(numbers)
    for n in numbers:
        if n < numbers[0]:
            numbers.insert(0,n)
    print(numbers)
#     x = int(asc_numbers[0])
#     for n in asc_numbers:
#         if n == x:
#             x = x + 1
#         else:
#             return False
#     return True
# output = is_consecutive_sequence(num1_list,num2_list)
# print(output)
