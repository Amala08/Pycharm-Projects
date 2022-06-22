statement = input("Enter a statement:")
statement_list = statement.split(" ")
def rev(message):
    output = " "
    for word in message:
        a = word[:-1]
        output += a + " "
    print(f"The reverse of the given statement is{output}")
rev(statement_list)