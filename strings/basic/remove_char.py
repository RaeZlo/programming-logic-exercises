"""
Your goal is to create a function that removes the first and last characters of a string. 
You're given one parameter, the original string. You don't have to worry about strings with less 
than two characters.

URL: https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0
"""





def remove_char(text: str) -> str:
    """
    Esta función recibe una cadena de texto y elimina el primer y último carácter de la cadena.
    
    Args:
        text (str): La cadena de texto original.
        
    Returns:
        str: La cadena resultante después de eliminar el primer y último carácter.
    """
    return text[1:-1]

# Pruebas de ejemplo
test1 = remove_char("Hola")
print(f"Resultado de la prueba 1: {test1}")  # Esperado: "ol"

test2 = remove_char("Python")
print(f"Resultado de la prueba 2: {test2}")  # Esperado: "ytho"
