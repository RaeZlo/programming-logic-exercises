"""
Write a function that takes a single non-empty string of only lowercase and uppercase 
ascii letters (word) as its argument, and returns an ordered list containing the indices 
of all capital (uppercase) letters in the string.

URL: https://www.codewars.com/kata/539ee3b6757843632d00026b
"""





def capitals(word: str) -> list[int]:
    """
    Devuelve una lista con los índices de todas las letras mayúsculas en la palabra dada.

    Args:
        word (str): Cadena de texto con solo letras mayúsculas y minúsculas.

    Returns:
        list[int]: Lista de índices de las letras mayúsculas en la cadena.
    """
    index_list = []  # Lista donde se guardarán los índices de las letras mayúsculas
    for index, char in enumerate(word):  # Itera sobre cada letra y su índice
        if char.isupper():  # Verifica si la letra es mayúscula
            index_list.append(index)  # Si es mayúscula, agrega el índice a la lista
    return index_list  # Devuelve la lista de índices

def capitals_alt(word: str) -> list[int]:
    """
    Devuelve una lista con los índices de todas las letras mayúsculas en la palabra dada usando comprensión de listas.

    Args:
        word (str): Cadena de texto con solo letras mayúsculas y minúsculas.

    Returns:
        list[int]: Lista de índices de las letras mayúsculas en la cadena.
    """
    return [index for index, char in enumerate(word) if char.isupper()] 

print(capitals("CodEWaRs"))  # Esperado: [0, 3, 4, 6]
print(capitals("abcD"))  # Esperado: [3]
print(capitals("hello"))  # Esperado: []
