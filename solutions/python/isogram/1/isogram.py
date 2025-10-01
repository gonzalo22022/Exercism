def is_isogram(string):
    
    letras_almacenadas=set()
    for letra in string.lower():
        if letra in [' ', '-']:
            continue 
        if letra in letras_almacenadas:
            return False
        letras_almacenadas.add(letra)    
    return True  
