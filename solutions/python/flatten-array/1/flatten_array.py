def flatten(iterable):
    resultado = []
    for elemento in iterable:
        if elemento != None:  
            if isinstance (elemento,list):
                resultado.extend(flatten(elemento))
            else:
                resultado.append(elemento)                    
    return resultado                        