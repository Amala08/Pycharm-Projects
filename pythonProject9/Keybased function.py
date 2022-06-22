#Keyword based argument
a = int(input("Enter any number: "))
b = int(input("Enter any number: "))
def calculate(num1,num2,operation):
    if operation == "add":
        print(f"The Result is {num1 + num2}")
    elif operation == "sub":
        print(f"The Result is {num1 - num2}")
    elif operation == "multiply":
        print(f"The Result is {num1 * num2}")
    elif operation == "division":
        print(f"The Result is {num1 / num2}")
calculate(num2=b, operation ="multiply", num1=a)
