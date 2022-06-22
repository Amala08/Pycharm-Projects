#list the even number words from the user statement
sentence = input("Enter the sentence:")
sentence_list = sentence.split(" ")
output_list = []
output = ""
for word in sentence_list:
    length = len(word)
    if length % 2 == 0:
        output_list.append(word)
for word in output_list:
    output += word + "\n"
print(f"The Even words from the given statement:\n{output}")



