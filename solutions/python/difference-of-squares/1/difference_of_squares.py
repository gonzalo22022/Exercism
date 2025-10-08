def square_of_sum(number):
    resultado = 0
    for numero in range(1, number+1):
        resultado += numero
    return (resultado**2)        
    

def sum_of_squares(number):
    resultado = 0
    for numero in range(1,number+1):
        resultado += (numero**2)
    return resultado     
    


def difference_of_squares(number):
    
    resultado = square_of_sum(number) - sum_of_squares(number)
    return resultado