"""
Given an integral number, determine if it's a square number:
In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words,
it is the product of some integer with itself.
"""





def is_square(num: int) -> bool:
    """
    En esta función, verificamos si un número es un cuadrado perfecto.
    Un número es un cuadrado perfecto si su raíz cuadrada es un número entero.
    
    Args:
        num (int): El número a evaluar.
        
    Returns:
        bool: True si el número es un cuadrado perfecto, False si no lo es.
    """
    return num >= 0 and (num ** 0.5) % 1 == 0

test1 = is_square(5)
print(f"¿El número 5 es un cuadrado perfecto? {test1}.")  # Esperado: False

test2 = is_square(16)
print(f"¿El número 16 es un cuadrado perfecto? {test2}.")  # Esperado: True
