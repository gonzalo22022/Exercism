def is_pangram(sentence):
    letras = 'abcdefghijklmnopqrstuvwxyz'

    sentence_e = sentence.lower()
    
    for letra in letras:
        if letra not in sentence_e:
            return False
    
    return True   








