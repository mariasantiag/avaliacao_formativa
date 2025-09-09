def classificar_triangulo(a: float, b: float, c: float):
    if not isinstance(a, (int, float)):
        raise TypeError("Os valores devem ser numéricos")
    if a < 0:
        raise ValueError("devem ser valores não-negativos")
    
    
    if not isinstance(b, (int, float)):
        raise TypeError("Os valores devem ser numéricos")
    if b < 0:
        raise ValueError("devem ser valores não-negativos")
    

    if not isinstance(c, (int, float)):
        raise TypeError("Os valores devem ser numéricos")
    if c < 0:
        raise ValueError("devem ser valores não-negativos")