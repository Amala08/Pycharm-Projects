name = input("Enter any name: ")
names = input("Enter any name: ")
namess = input("Enter any name: ")
name1 = name.lower()
name2 = names.lower()
name3 = namess.lower()
count1 = 0
count2 = 0
count3 = 0
count = 0
matching_char1 = ""
matching_char2 = ""
matching_char3 = ""
matching_char = ""
for n in name1:
    if name2.find(n) >= 0 and n not in matching_char1:
        matching_char1 += n
        count1 += 1
for a in name2:
    if name3.find(a) >= 0 and a not in matching_char2:
        matching_char2 += a
        count2 += 1
for m in name1:
    if name3.find(m) >= 0 and m not in matching_char3:
        matching_char3 += m
        count3 += 1
for char1 in matching_char1:
    if char1 in matching_char2:
        if char1 in matching_char3:
            matching_char += char1 +"\n"
            count += 1
print(matching_char)
print(count)