def transform(legacy_data):
    resultado= {}
    for puntaje, letras in legacy_data.items():
        for letra in letras:
            resultado[letra.lower()] = puntaje
    return resultado       