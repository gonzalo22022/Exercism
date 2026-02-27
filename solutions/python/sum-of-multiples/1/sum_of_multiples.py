def sum_of_multiples(limit, multiples):
    resultado = set()
    for numero in multiples:
        if numero == 0:
            continue
        for numero2 in range(numero, limit, numero):
            resultado.add(numero2)
        
    return sum(resultado)