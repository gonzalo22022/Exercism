colores = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']

def label(colors):
    primerosDos = colors[:2]
    ultimo = colors[2]
    numerosDos = [colores.index(color) for color in primerosDos]
    ultimoNumero = colores.index(ultimo)

    numeroDostxt = int(''.join([str(d) for d in numerosDos]))
    
    valor_final = numeroDostxt * (10 ** ultimoNumero)

    if valor_final < 1000:
        return f'{valor_final} ohms'
        
    if valor_final <1_000_000:
        return f'{valor_final //1000} kiloohms'
         
    elif valor_final < 1_000_000_000:
        return f'{valor_final //1_000_000} megaohms'       
    else:
        return f'{valor_final // 1_000_000_000} gigaohms'