#Check whether user string starts with the given string
my_str = "Friends, We love programming"
search_str = input("Enter a word or statement : ")
start_str = search_str.startswith("Friends")#using stratswith function comparing both the strings first word
print(start_str)