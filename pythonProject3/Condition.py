height = int(input("Enter the height in cm :"))

if height >= 120:
  print("You are allowed to ride")
  age = int(input("Enter your age: "))
  if age > 18:
      print("Your ticket rate is $12")
  else:
      print("Your ticket rate is $7")

else:
    print("You are not allowed to ride")
