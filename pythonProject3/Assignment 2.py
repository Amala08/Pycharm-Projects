total_bill = float(input("Enter your total bill amount : $"))
tips = float(input("Enter the Tip amount : "))
friends = int(input("How many people to split the bill : "))
tips_in_amt = (total_bill * tips)/100 #tips calculation
per_person = round((total_bill + tips_in_amt)/friends,2)
print(f"Each person has to pay ${per_person}")