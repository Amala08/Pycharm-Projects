#using for loop method and remove function to remove the blank element in list
names = input("Enter list of names with empty space: ")
name_list = names.split(",")
print(f"names_list = {name_list}")
for name in name_list:
    if name == ' ':
        name_list.remove(name)
print(f"The Output is {name_list}")
