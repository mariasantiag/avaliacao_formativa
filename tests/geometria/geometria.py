def classificar_triangulo(a: float, b: float, c: float):
    if not isinstance(a, (int, float)):
        raise TypeError("Os valores devem ser numéricos.")
    if a < 0:
        raise ValueError("Lados devem ser positivos.")
    

    if not isinstance(b, (int, float)):
        raise TypeError("Os valores devem ser numéricos.")
    if b < 0:
        raise ValueError("Lados devem ser positivos.")
    

    if not isinstance(c, (int, float)):
        raise TypeError("Os valores devem ser numéricos.")
    if c < 0:
        raise ValueError("Lados devem ser positivos.")

    
    if a + b < c:
        raise ValueError("Lados não formam um triângulo.")
    
    if a + c < b:
        raise ValueError("Lados não formam um triângulo.")
    
    if b + c < b:
        raise ValueError("Lados não formam um triângulo.")
    
    

    if a == b and b == c and c == a:
        return "Equilátero"
    elif a == b or b == c or c == a:
        return "Isósceles"
    else:
        return "Escaleno"