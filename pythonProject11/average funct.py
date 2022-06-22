number = input("Enter the list of numbers: ").split(",")
size = len(number)
for n in range(size):
   number[n] = int(number[n])
count = size
add = 0
def average(user_number,count,add):
    while count > 0:
        for i in user_number:
            add = add + i
            count = count - 1
    avg = add / size
    print(f"The average for the given number is: {avg}")
average(number,count,add)