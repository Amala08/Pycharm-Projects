numbers = input("Enter the numbers : ").split(",")
num = []
for n in numbers:
    n0 = n
    n1 = numbers[-1]
    if n0 == n1:
        num.append(n0)
    else:
        num.append(n0)
        num.append(n1)
        numbers.remove(n1)
print(num)
