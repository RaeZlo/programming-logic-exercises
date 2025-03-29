"""
You have two lists of strings, a1 and a2. You need to return a new list with the words from a1 that are substrings of any word in a2. 
The list should be sorted in lexicographical order.

Example 1: 
a1 = ["arp", "live", "strong"] 
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

Result: ["arp", "live", "strong"]

Notes:
The resulting list should not have duplicate elements.

URL: https://www.codewars.com/kata/550554fd08b86f84fe000a58
"""





def in_array(array1: list[str], array2: list[str]) -> list[str]:
    """
    Itera sobre cada palabra en `array1` y verifica si es una subcadena de alguna palabra en `array2`.
    Si la palabra está en `array2` y aún no está en `result`, se agrega a la lista.
    
    Args:
        array1 (list[str]): Lista de palabras a buscar como subcadenas.
        array2 (list[str]): Lista de palabras en las que se buscan las subcadenas.
    
    Returns:
        list[str]: Lista ordenada alfabéticamente con las palabras encontradas.
    """
    result = []  # Lista para almacenar las palabras encontradas
    # Recorremos cada palabra de `array1`
    for a1 in array1:
        # Recorremos cada palabra de `array2`
        for a2 in array2:
            # Verificamos si `a1` es subcadena de `a2` y que no esté duplicada en `result`
            if a1 in a2 and a1 not in result:
                result.append(a1)
    # Ordenamos el resultado en orden lexicográfico
    result.sort()
    return result


def in_array_alt(array1: list[str], array2: list[str]) -> list[str]:
    """
    Versión alternativa utilizando comprensión de listas y `any()`.
    Se filtran las palabras de `array1` que sean subcadenas de alguna palabra en `array2`.
    Luego se convierte el resultado en un conjunto para eliminar duplicados y se ordena.

    Args:
        array1 (list[str]): Lista de palabras a buscar como subcadenas.
        array2 (list[str]): Lista de palabras en las que se buscan las subcadenas.

    Returns:
        list[str]: Lista ordenada alfabéticamente con las palabras encontradas.
    """
    result = [word1 for word1 in array1 if any(word1 in word2 for word2 in array2)]
    return sorted(set(result))



a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

print(in_array(a1, a2))  # ["arp", "live", "strong"]
print(in_array_alt(a1, a2))  # ["arp", "live", "strong"]
