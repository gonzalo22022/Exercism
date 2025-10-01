def is_valid(isbn):
    texto= isbn.replace('-', '')
    if len(texto) != 10:
        return False
    suma= 0
    for indice in range(10):
        
        char = texto[indice]
        
        if indice == 9 :
            if char == 'X':
                valor = 10
            elif char.isdigit():
                valor = int(char)
            else:
                return False
        else:
            if not char.isdigit():
                return False
            valor = int(char)    
        
        peso = 10 - indice
        suma += valor * peso
    if suma % 11 == 0:
        return True
    return False        
    
            