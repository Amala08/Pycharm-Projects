#find Match char b/w two strings and get the count, ignore repeated ones
name1 = input("Enter any name: ").lower()
name2 = input("Enter any name: ").lower()
#to convert in lowercase
#name1 = name.lower()
#name2 = names.lower()
count = 0
matching_char = ""
#name1 = Amala
#name2 = Hari
for n in name1:
     if name2.find(n) >= 0 and n not in matching_char:#to check if name each char are there in names and to remove if it is repeated
        matching_char += n + "\n"
        count = count + 1
print(f"Matching characters :\n{matching_char}")
print(f"Matching characters Count :\n{count}")

