"""
Write a function to split a string and convert it into an array of words.

URL: https://www.codewars.com/kata/57e76bc428d6fbc2d500036d
"""





def string_to_array(text: str) -> list[str]:
    """
    Esta función recibe un string y lo divide en una lista de palabras separadas por espacios.

    Args:
        text (str): Una cadena de texto.

    Returns:
        list[str]: Una lista con las palabras de la cadena original.
    """
    return text.split(" ")


print(string_to_array("Hola mundo"))       # Esperado: ['Hola', 'mundo']
print(string_to_array("Python es genial")) # Esperado: ['Python', 'es', 'genial']
print(string_to_array(""))                 # Esperado: [''] (caso borde con cadena vacía)
print(string_to_array("   "))              # Esperado: ['', '', '', ''] (caso borde con solo espacios)
