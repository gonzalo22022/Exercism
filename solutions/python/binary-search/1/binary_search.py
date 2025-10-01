def find(search_list, value):

    izquierda = 0
    derecha = len(search_list) - 1

    while izquierda <= derecha:
        mitad = (izquierda + derecha) // 2
        if search_list[mitad] == value:
            return mitad 
        elif search_list[mitad] < value:
            izquierda = mitad + 1
        else:
            derecha = mitad - 1

    raise ValueError("value not in array")
            