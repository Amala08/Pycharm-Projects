items = input("Enter any list of elements: ")
list1 = items.split(",")
print(f"User list = {list1}")
size = len(list1)
list2 = []
x = 0
y = size - 1
while x < y:
    first = list1[x]
    list2.append(first)
    x = x + 1
    last = list1[y]
    list2.append(last)
    y = y - 1
if x == y:
    first = list1[x]
    list2.append(first)
print(f"The Output is {list2}")
