def is_armstrong_number(number):
    digitos = str(number)
    cantidad_d= len(digitos)
    suma = sum(int(dig)**cantidad_d for dig in digitos)
    
    return suma == number
    