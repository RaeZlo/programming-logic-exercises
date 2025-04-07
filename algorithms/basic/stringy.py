"""
write me a function stringy that takes a size and returns a string of alternating 1s and 0s.
the string should start with a 1.

URL: https://www.codewars.com/kata/563b74ddd19a3ad462000054
"""





def stringy(size: int) -> str:
    """
    Genera un string de longitud `size` con 1s y 0s alternados, comenzando por 1.

    Args:
        size (int): Longitud del string a generar.

    Returns:
        str: Cadena de 1s y 0s alternados comenzando con 1.
    """
    return "".join("1" if i % 2 == 0 else "0" for i in range(size))


def stringy_alt(size: int) -> str:
    """
    Alternativa que genera la cadena repitiendo '10' y cortando al tamaño deseado.

    Args:
        size (int): Longitud del string a generar.

    Returns:
        str: Cadena de 1s y 0s alternados comenzando con 1.
    """
    return ('10' * size)[:size]


print(stringy(6))      # '101010'
print(stringy(7))      # '1010101'
print(stringy_alt(6))  # '101010'
print(stringy_alt(7))  # '1010101'
