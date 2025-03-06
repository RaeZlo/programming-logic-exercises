"""
Write a function which converts the input string to uppercase.

URL: https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7
"""





def make_upper_case(text:str) -> str:
    """
    Esta función recibe una cadena de texto y la convierte a mayúsculas.
    
    Args:
        text (str): La cadena de texto que se desea convertir.
        
    Returns:
        str: La cadena de texto en mayúsculas.
    """
    return text.upper()

# Ejemplo de prueba
test1 = make_upper_case("hola mundo")
print(f"Texto en mayúsculas: {test1}")  # Esperado: "HOLA MUNDO"

test2 = make_upper_case("Python es genial")
print(f"Texto en mayúsculas: {test2}")  # Esperado: "PYTHON ES GENIAL"
