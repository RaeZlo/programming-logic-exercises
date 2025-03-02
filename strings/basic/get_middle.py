"""
You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.
If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.

URL: https://www.codewars.com/kata/56747fd5cb988479af000028
"""





def get_middle(text: str) -> str:
    """
    En esta función, se recibe una cadena de texto y se devuelve el o los caracteres del medio. 
    Si la longitud de la cadena es impar, se devuelve el carácter central. 
    Si la longitud es par, se devuelven los dos caracteres centrales.
    
    Args:
        text (str): La cadena de texto cuya parte central se debe obtener.
        
    Returns:
        str: El carácter o los dos caracteres del medio de la cadena.
    """
    middle = len(text) // 2
    return text[middle - 1:middle + 1] if len(text) % 2 == 0 else text[middle]

test1 = get_middle("test")
print(test1)  # Esperado: "es"

test2 = get_middle("testing")
print(test2)  # Esperado: "t"
