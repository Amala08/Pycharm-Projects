name = input("Enter the Player name: ")
for n in range(1,101):
    if n % 5 == 0 and n % 7 == 0:
        print(f"Hello,{name}")
    elif n % 7 == 0:
        print(f"{name}")
    elif n % 5 == 0:
        print("Hello")
    else:
        print(n)

