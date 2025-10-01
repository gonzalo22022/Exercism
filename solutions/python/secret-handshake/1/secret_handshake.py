def commands(binary_str):
    primerN = binary_str[-1]
    segundN = binary_str[-2]
    tercerN = binary_str[-3]
    cuartoN = binary_str[-4]
    quinto = binary_str[-5]
   
    listaAcciones =[]
    if int(primerN) == 1:
        listaAcciones.append('wink')
    if int(segundN) == 1:
        listaAcciones.append('double blink')
    if int(tercerN) == 1:
        listaAcciones.append('close your eyes')
    if int(cuartoN) == 1:
        listaAcciones.append('jump')
    if int(quinto) == 1:
        listaAcciones.reverse()

    return listaAcciones
        
        