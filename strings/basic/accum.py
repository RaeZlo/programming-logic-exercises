"""
In this task, you are given a string. Your goal is to return a new string where each character in the 
original string is repeated a number of times equal to its position in the string (starting from 1), 
and each repeated character is capitalized in a specific pattern. The characters are joined by hyphens.
Example:
accum("abcd") should return "A-Bb-Ccc-Dddd"

URL: https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
"""





def accum(text: str) -> str:
    """
    En esta función, tomamos una cadena de texto y devolvemos una nueva cadena en la que cada carácter de la 
    cadena original se repite un número de veces igual a su posición en la cadena (empezando desde 1), y cada 
    carácter repetido se pone en un patrón de mayúsculas y minúsculas. Los caracteres repetidos están separados por guiones.
    
    Args:
        text (str): La cadena de texto a procesar.
        
    Returns:
        str: La nueva cadena con los caracteres repetidos y formateados.
    """
    return "-".join((char * (index + 1)).capitalize() for index, char in enumerate(text))

# Pruebas de la función
test1 = accum("abcd")
print(test1)  # Esperado: "A-Bb-Ccc-Dddd"

test2 = accum("cwAt")
print(test2)  # Esperado: "C-Ww-Aaa-Tttt"
