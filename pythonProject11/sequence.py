def is_consecutive_sequence(number1,number2):
    number = number1 + number2
    numbers = []
    for n in number:
        if n not in numbers:
            numbers.append(n)
    asc_numbers = sorted(numbers)
    x = int(asc_numbers[0])
    for n in asc_numbers:
        if n == x:
            x = x + 1
        else:
            return False
    return True

