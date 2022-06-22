num = input("Enter the number : ")
low = []
high = []
for n in num:
    sort_numb = sorted(num,reverse=True)
high = high + sort_numb
for n in num:
    sort_num = sorted(num)
low = low + sort_num
for i in low:
    x = int("". join(low))
for i in high:
    y = int("".join(high))
print("Lowest number : ", x)
print("Highest number : ", y)
diff = y - x
print(f"The diff is {diff}")