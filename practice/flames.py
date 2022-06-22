name1 = input("Enter any name: ")
name2 = input("Enter any name: ")
name1_list = list(name1)
name2_list = list(name2)
total_letter = []
for name in name1_list:
    if name in name2_list:
        name2_list.remove(name)
        name1_list.remove(name)
    else:
        total_letter.append(name)
print(total_letter)
for name in name2_list:
    if name in name1_list:
        name2_list.remove(name)
        name1_list.remove(name)
    else:
        total_letter.append(name)
    print(total_letter)
size = len(total_letter)
print(size)
lists = ["F", "l", "a", "m", "e", "s"]
count = len(lists)
while count > 0:
    n = size - (count+1)
    for i in lists:
        if n >= 0:
            lists.pop(n)
    count = count -1







