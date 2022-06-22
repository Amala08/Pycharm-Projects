def calc(num1, num2, operation):
    if operation == 'Addition':
        c = num1 + num2
        print(f"Addition of {num1} and {num2} is {c}")
    elif operation == 'Subtract':
        c = num1 - num2
        print(f"Subtraction of {num1} and {num2} is {c}")
    elif operation == 'Product':
        c = num1 * num2
        print(f"Product of {num1} and {num2} is {c}")
    elif operation == 'Division':
        c = num1 / num2
        print(f"Quotient of {num1} and {num2} is {c}")
    else:
        print("Invalid Operation")

operation_choice = input("Enter the operation you want to perform  : ")
operation_dict = {"+":"Addition", "-": "Subtract", "*": "Product", "/": "Division"}
while operation_choice != '+' and operation_choice != '-' and operation_choice != '*' and operation_choice != '/':
    operation_choice = input("Please Enter Valid Operation (Addition/Subtract/Multiply/Division) : ")

num1 = input("Enter first number : ")
num2 = input("Enter second number : ")

while not num1.isdigit() or not num2.isdigit():
    print('Please Enter valid Numbers only in Digits ')
    num1 =  input("Enter first number : ")
    num2 = input("Enter second number : ")
calc(int(num1), int(num2), operation_dict.get(operation_choice))