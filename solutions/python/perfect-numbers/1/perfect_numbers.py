def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <=0:
        raise ValueError("Classification is only possible for positive integers.")
    resultado= 0
    for numero in range(1,number//2+1):
        if number % numero == 0 :
            resultado += numero
    if resultado == number:
        return 'perfect'
    elif resultado < number:
        return 'deficient'
    else:
        return 'abundant'