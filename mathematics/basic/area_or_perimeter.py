"""
You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
If it is a square, return its area. If it is a rectangle, return its perimeter.

URL: https://www.codewars.com/kata/5ab6538b379d20ad880000ab
"""





def area_or_perimeter(length: int, width: int) -> int:
    """
    En esta función, verificamos si el polígrafo es un cuadrado o un rectángulo. 
    Si es un cuadrado (es decir, la longitud y el ancho son iguales), 
    devolvemos el área del cuadrado. Si es un rectángulo, devolvemos su perímetro.
    
    Args:
        length (int): La longitud del polígono.
        width (int): El ancho del polígono.
        
    Returns:
        int: El área del cuadrado o el perímetro del rectángulo.
    """
    return length * width if length == width else 2 * (length + width)

# Pruebas de la función
test1 = area_or_perimeter(4, 4)
print(f"El resultado es: {test1}")  # Esperado: 16 (área de un cuadrado)

test2 = area_or_perimeter(4, 6)
print(f"El resultado es: {test2}")  # Esperado: 20 (perímetro de un rectángulo)
