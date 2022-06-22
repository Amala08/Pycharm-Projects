number = int(input("Enter any number: "))
power = int(input("Enter the exponentiation power: "))
def exp(base,exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * exp(base,exponent-1)
    else:
        return 1 / exp(base,-exponent)
result = exp(number,power)
print(f"The Output is {result}")