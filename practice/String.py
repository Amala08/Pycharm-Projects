statement = input("Enter any statement: ").lower().split(" ")
size = len(statement)
output = ""
x = 0
while size >= x:
    for i in statement[0]:
        for j in statement[x]:
            if i == j and i not in output:
                output += i
    x += 1
print(f"The common sub string in given statement is {output}")
