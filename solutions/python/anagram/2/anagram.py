def find_anagrams(word, candidates):
    resultado = []
    palabra = word.lower()
    
   
        
    for candidato in candidates:
        if len(word) == len(candidato) :
            if sorted(candidato.lower()) == sorted(palabra):
                if candidato.lower() != palabra:
                    resultado.append(candidato)
            
    return resultado
                
        
        