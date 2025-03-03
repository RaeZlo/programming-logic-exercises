"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.

URL: https://www.codewars.com/kata/54ba84be607a92aa900000f1
"""





def is_isogram(string: str) -> bool:
    """
    Esta función recibe una cadena de texto y determina si es un isograma. Un isograma es una palabra 
    que no tiene letras repetidas, consecutivas o no consecutivas. 
    La comparación no distingue entre mayúsculas y minúsculas.
    
    Args:
        string (str): La cadena de texto a evaluar.
        
    Returns:
        bool: Retorna True si la cadena es un isograma, False en caso contrario.
    """
    return len(set(string.lower())) == len(string)

def is_isogram_alt(string: str) -> bool:
    """
    Esta función alternativa recibe una cadena de texto y verifica si es un isograma. Recorre la cadena 
    y comprueba si alguna letra se repite más de una vez, ignorando mayúsculas y minúsculas.
    
    Args:
        string (str): La cadena de texto a evaluar.
        
    Returns:
        bool: Retorna True si la cadena es un isograma, False en caso contrario.
    """
    for char in string.lower(): 
        if string.count(char) > 1:
            return False
    return True

test1 = is_isogram("Dermatoglyphics")
print(f"Resultado de la prueba 1: {test1}")  # Esperado: True

test2 = is_isogram("aba")
print(f"Resultado de la prueba 2: {test2}")  # Esperado: False

test3 = is_isogram_alt("Dermatoglyphics")
print(f"Resultado de la prueba 3: {test3}")  # Esperado: True

test4 = is_isogram_alt("aba")
print(f"Resultado de la prueba 4: {test4}")  # Esperado: False
