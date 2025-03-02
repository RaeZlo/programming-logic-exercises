"""
In this task, you are given a string, and your goal is to return the string with its characters reversed.

URL: https://www.codewars.com/kata/5168bb5dfe9a00b126000018
"""





def reversed_strings(text: str) -> str:
    """
    En esta función, tomamos una cadena de texto y devolvemos la misma cadena 
    pero con los caracteres en orden inverso.
    
    Args:
        text (str): La cadena de texto a invertir.
        
    Returns:
        str: La cadena de texto con los caracteres en orden inverso.
    """
    return text[::-1]

test1 = reversed_strings('world')
print(test1)  # Esperado: "dlrow"

test2 = reversed_strings('Python')
print(test2)  # Esperado: "nohtyP
