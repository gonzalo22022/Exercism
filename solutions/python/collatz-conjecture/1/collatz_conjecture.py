def steps(number):
    if number <= 0:   
        raise ValueError("Only positive integers are allowed")    

    cuenta = 0
    while number != 1 :
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        cuenta += 1
    return cuenta    