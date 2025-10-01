def square(number):
    number = int(number)
    resultado = 0
    if 1 <= number <= 64 :
        resultado_f = 2 ** (number-1)
        return resultado_f 
    
    raise ValueError("square must be between 1 and 64")      
        
        


def total():

    return sum( 2 ** numero for numero in range(64))
    