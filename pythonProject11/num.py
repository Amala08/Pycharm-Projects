import oddevn_func
lower_bound = int(input("Enter a number: "))
upper_bound = int(input("Enter a number greater than previous number: "))
output = oddevn_func.even_sum_digit(lower_bound,upper_bound)
if output == []:
    print("There is no Even number in the given range")
else:
    print(f"The Even numbers are {output}")
