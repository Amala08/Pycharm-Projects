#Count the  character in string
my_str = input("Enter any statement: ")
search_char = input("Enter any character : ")
count_char = my_str.count(search_char) #using count function checking how many times character displayed in the string
print("The character " + search_char + " occurred " + str(count_char) + " times in " + my_str)