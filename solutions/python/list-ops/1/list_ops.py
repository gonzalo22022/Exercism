def append(list1, list2):
    resultado =[]
    for item in list1:
        resultado.append(item)
    for itemdos in list2:
        resultado.append(itemdos)
    return resultado

def concat(lists):
    resultado = []
    for lista in lists:
        for elemento in lista:
            resultado.append(elemento)
    return resultado    

def filter(function, list):

    resultado = []
    for elemento in list:
        if function(elemento):
            resultado.append(elemento)
        
            
    return resultado

def length(list):

    resultado = 0
    for item in list:
        resultado+= 1
    return resultado

def map(function, list):
    resultado=[]
    for elemento in list:
        resultado.append(function(elemento))
    return resultado
    

def foldl(function, list, initial):
    acumulador = initial
    for elemento in list:
        acumulador = function(acumulador, elemento)
    return acumulador    


def foldr(function, list, initial):
    acumulador = initial
    lista=reversed(list)
    for elemento in lista:
        acumulador = function(acumulador, elemento)
    return acumulador   


def reverse(list):

    resultado = []
    for elemento in list:
        resultado.insert(0,elemento)
    return resultado
    
