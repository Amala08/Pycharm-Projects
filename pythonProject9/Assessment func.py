#default based argument
num1 = int(input("Enter any number: "))
num2 = int(input("Enter any number: "))
def calculate(num1,num2,operation="multiply"):
    if operation == "add":
        print(f"The Result is {num1 + num2}")
    elif operation == "sub":
        print(f"The Result is {num1 - num2}")
    elif operation == "multiply":
        print(f"The Result is {num1 * num2}")
    elif operation == "division":
        print(f"The Result is {num1 / num2}")
calculate(num1, num2)
#Position based argument
def calculate(num1,num2,operation):
    num1 = int(input("Enter any number: "))
    num2 = int(input("Enter any number: "))
    if operation == "add":
        print(f"The Result is {num1 + num2}")
    elif operation == "sub":
        print(f"The Result is {num1 - num2}")
    elif operation == "multiply":
        print(f"The Result is {num1 * num2}")
    elif operation == "division":
        print(f"The Result is {num1 / num2}")
calculate(num1,num2,"sub")
