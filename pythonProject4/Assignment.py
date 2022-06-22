import random
name = input("Enter the list of names : \n")
name_list = name.split(" ") #Command to assign the string value to list by splitting the space/comma
print(name_list)
size = len(name_list) #To find the size of the list
print(f"The size of the list is {size}")
#Using random module to choose the random name
choice = random.randint(0,size-1)
print(f"Chosen name is {name_list[choice]}")






