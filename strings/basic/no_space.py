"""
Write a function that removes the spaces from the string, then return the resultant string.

URL: https://www.codewars.com/kata/57eae20f5500ad98e50002c5
"""





def no_space(text: str) -> str:
    """
    Esta función recibe una cadena de texto y elimina todos los espacios en blanco que contiene,
    devolviendo la cadena resultante sin espacios.
    
    Args:
        text (str): La cadena de texto a procesar.
        
    Returns:
        str: La cadena de texto sin espacios.
    """
    return text.replace(" ", "")

# Pruebas de ejemplo
test1 = no_space("Hello World")
print(f"Resultado de la prueba 1: {test1}")  # Esperado: "HelloWorld"

test2 = no_space("This is a test")
print(f"Resultado de la prueba 2: {test2}")  # Esperado: "Thisisatest"
