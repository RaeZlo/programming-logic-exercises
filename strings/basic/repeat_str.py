"""
Write a function that accepts a non-negative integer n and a string s as parameters, and returns 
a string of s repeated exactly n times.

URL: https://www.codewars.com/kata/57a0e5c372292dd76d000d7e
"""





def repeat_str(repeat: int, string: str) -> str:
    """
    Esta función recibe un número entero no negativo y una cadena de texto, y retorna una nueva cadena
    en la que la cadena de texto se repite exactamente el número de veces indicado por el número entero.
    
    Args:
        repeat (int): El número de veces que se repetirá la cadena.
        string (str): La cadena de texto que se repetirá.
        
    Returns:
        str: La cadena de texto repetida exactamente 'repeat' veces.
    """
    return string * repeat

# Pruebas de ejemplo
test1 = repeat_str(3, "abc ")
print(f"Resultado de la prueba 1: {test1}")  # Esperado: "abc abc abc "

test2 = repeat_str(5, "hello ")
print(f"Resultado de la prueba 2: {test2}")  # Esperado: "hello hello hello hello hello "
