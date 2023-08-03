def is_prime(number):
    flag = False
    if number == 1:
        return str(False)
    elif number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                flag = True
                break
        if flag:
            return str(False)
    else:
        return str(True)
