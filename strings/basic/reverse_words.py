"""
Complete the function that accepts a string parameter, and reverses each word in the string. 
All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"

URL: https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
"""





def reverse_words(text: str) -> str:
    """
    Esta función recibe una cadena de texto y revierte cada palabra dentro de la cadena,
    manteniendo los espacios en su lugar.

    Args:
        text (str): La cadena de texto que contiene las palabras a invertir.

    Returns:
        str: La cadena de texto con cada palabra invertida, manteniendo los espacios.
    """
    return " ".join(word[::-1] for word in text.split(' '))

test1 = reverse_words("This is an example!")
print(test1)  # Esperado: "sihT si na !elpmaxe"

test2 = reverse_words("double  spaces")
print(test2)  # Esperado: "elbuod  secaps"
