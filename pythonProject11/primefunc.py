lower_bound = int(input("Enter a number: "))
upper_bound = int(input("Enter a number greater than previous number: "))
prime_number = []
def primenumber(lowest,highest):
    for num in range(lowest,highest+1):#11,21
        if num == 2:
            prime_number.append(num)
        else:
            for n in range(2,int(num/2)):
                if num % n == 0:
                    break
            else:
                if num not in prime_number and num != 1:
                    prime_number.append(num)
    output = ",".join(map(str,prime_number))
    print(f"The Prime Numbers are {output}")
primenumber(lower_bound,upper_bound)