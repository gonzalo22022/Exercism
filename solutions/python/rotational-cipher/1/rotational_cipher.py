def rotate(text, key):
    resultado=[]
    for char in text:
        if not char.isalpha():
                    resultado.append(char)
                    continue
        if char.islower():
            base = ord('a')
            nueva_letra = chr((ord(char)- base + key) % 26 + base)
            resultado.append(nueva_letra)
        elif char.isupper():
            base = ord('A')
            nueva_letra = chr((ord(char)- base + key) % 26 + base)
            resultado.append(nueva_letra)
        else:
            resultado.append(char)
    return ''.join(resultado)               
        
        
                                  
                                        
                        
    