num = input("Enter any number: ")
num_list = list(num)
print(num_list)
size = len(num_list)
x = 0
output = ""
n = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",  8: "Eight", 9: "Nine"}
while size > x:
    word = n[int(num_list[x])]
    x += 1
    output += word + " "
print(f"The Output of the given number '{num}' is {output}")