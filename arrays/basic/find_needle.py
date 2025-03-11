"""
Write a function that takes an array full of junk but containing one "needle"
After your function finds the needle it should return a message (as a string) that says:
"found the needle at position " plus the index it found the needle.

URL: https://www.codewars.com/kata/56676e8fabd2d1ff3000000c
"""





def find_needle(haystack: list[str]) -> str:
    """
    En esta función, tomamos una lista de elementos que contiene una "aguja", y retornamos una cadena que indica
    la posición en la que se encuentra la aguja en el arreglo.
    
    Args:
        haystack (list[str]): Una lista de elementos que contiene una cadena "needle".
        
    Returns:
        str: Un mensaje indicando la posición de la aguja en el arreglo.
    """
    # Encontrar el índice de la "needle" y devolver el mensaje con el índice
    return f"found the needle at position {haystack.index('needle')}"

# Pruebas de la función
test1 = find_needle(['hay', 'needle', 'hay'])
print(test1)  # Esperado: "found the needle at position 1"

test2 = find_needle(['needle', 'hay', 'hay'])
print(test2)  # Esperado: "found the needle at position 0"
