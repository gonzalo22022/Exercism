def equilateral(sides):
    a, b ,c = sides
    
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b < c or b + c < a or a + c < b: 
        return False
    if a == b == c :
        return True
    return False
    


def isosceles(sides):
    a, b ,c = sides

    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b < c or b + c < a or a + c < b: 
        return False
    return a == b or c == a or c == b

def scalene(sides):
    a, b ,c = sides

    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b < c or b + c < a or a + c < b: 
        return False
    return a != b and b != c and a != c 
