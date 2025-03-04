"""
Write a function to convert a name into initials. Takes two words with one space in between them.
The output should be two capital letters with a dot separating them.

URL: https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
"""





def abbrev_name(name: str) -> str:
    """
    Esta función recibe un nombre compuesto por dos palabras separadas por un espacio
    y devuelve las iniciales en formato de letras mayúsculas, separadas por un punto.
    
    Args:
        name (str): El nombre que contiene dos palabras.
        
    Returns:
        str: Las iniciales del nombre, en formato de letras mayúsculas separadas por un punto.
    """
    return ".".join(char[0] for char in name.split()).upper()

test1 = abbrev_name("John Doe")
print(f"Resultado de la prueba 1: {test1}")  # Esperado: "J.D"

test2 = abbrev_name("Jane Smith")
print(f"Resultado de la prueba 2: {test2}")  # Esperado: "J.S"
