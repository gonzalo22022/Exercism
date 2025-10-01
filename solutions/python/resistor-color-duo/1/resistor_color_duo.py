colores = [
        "black", "brown", "red", "orange", "yellow",
        "green", "blue", "violet", "grey", "white"
    ]
def value(colors):
    p_dos= colors[:2]
 
    digitos = [colores.index(color) for color in p_dos]
    return int(''.join(map(str, digitos)))