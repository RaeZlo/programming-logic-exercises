"""
Write a function maskify(cc) that masks all but the last four characters of a given string cc with #. 
If the string is 4 characters or shorter, return it unchanged.
Example:
maskify("4556364607935616")  # Output: "############5616"

URL: https://www.codewars.com/kata/5412509bd436bd33920011bc
"""





def maskify(text: str) -> str:
    """
    Esta función recibe una cadena de texto y oculta todos los caracteres excepto los últimos cuatro,
    reemplazando con el símbolo '#' los caracteres anteriores.
    Si la cadena tiene 4 caracteres o menos, se devuelve sin modificaciones.
    
    Args:
        text (str): La cadena de texto a modificar.
        
    Returns:
        str: La cadena modificada con los primeros caracteres reemplazados por '#'.
    """
    return text if len(text) <= 4 else "#" * (len(text) - 4) + text[-4:]

# Pruebas de ejemplo
test1 = maskify("Skippy")
print(f"Resultado de la prueba 1: {test1}")  # Esperado: "##ippy"

test2 = maskify("4556364607935616")
print(f"Resultado de la prueba 2: {test2}")  # Esperado: "############5616"
