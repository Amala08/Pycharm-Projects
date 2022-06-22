#Reverse the list
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)

#Add new item
my_list = [1,2,3,4,5]
my_list.append(6)
my_list.append(7)
print(my_list)

#Remove a item
my_list = [1,2,3,4,5]
my_list.remove(5)
print(my_list)

#Replace in a list
my_list = [1,2,3,4,5]
index = my_list.index(3) #get the location of the value
my_list[index] = 0  #assign new value to that location
print(my_list)

#Add two or three item in a list
my_list = [1,2,3,4,5]
add_list = [6,7,8,9,10]
my_list.extend(add_list)
print(my_list)

#Print the last item using negative index in the list
my_list = [1,2,3,4,5]
print(my_list[-3])

#Insert an item in the middle of the string
my_list = [1,2,3,4,5]
my_list.insert(2,7)
print(my_list)


