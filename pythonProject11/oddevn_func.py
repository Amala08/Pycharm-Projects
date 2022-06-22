def even_sum_digit(lowest,highest):
    '''
    This functions take two parameter of number and checks if each digit in the number is even and returns the even number
    :param lowest:
    :param highest:
    :return:
    '''
    output = []
    for number in range(lowest, highest + 1):
        x = number
        size = len(str(x))
        while size > 0:
            if x % 2 == 0:
                x = x // 10
                size = size - 1
                if size == 0:
                    if number not in output:
                        output.append(number)
            else:
                break
    return output