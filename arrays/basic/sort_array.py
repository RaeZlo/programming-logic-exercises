"""
You are given an array of numbers. Your task is to sort only the odd numbers in ascending order, 
while keeping the even numbers in their original positions.

URL: https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
"""





def sort_array(source_array: list[int]) -> list[int]:
    """
    Ordena los números impares en orden ascendente, manteniendo los pares en su posición original.

    Args:
        source_array (list[int]): Lista de números enteros.

    Returns:
        list[int]: Lista con los impares ordenados y los pares en su posición original.
    """
    odd_numbers = sorted([num for num in source_array if num % 2 != 0])  # Lista de impares ordenados
    index = 0  # Índice para recorrer los impares ordenados
    result = []  # Lista resultado

    for num in source_array:
        if num % 2 != 0:  # Si el número es impar, lo sustituimos por el ordenado
            result.append(odd_numbers[index])
            index += 1
        else:  # Si es par, lo dejamos en su posición original
            result.append(num)
    
    return result


def sort_array_alt(arr: list[int]) -> list[int]:
    """
    Versión alternativa que utiliza pop() para extraer los números impares ordenados.
    """
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)  # Ordenamos impares en orden descendente
    # Usamos pop() para ir sacando los impares ordenados (en orden ascendente)
    return [x if x % 2 == 0 else odds.pop() for x in arr]


print(sort_array([5, 3, 2, 8, 1, 4]))  # [1, 3, 2, 8, 5, 4]
print(sort_array([9, 8, 7, 6, 5]))  # [5, 8, 7, 6, 9]
print(sort_array([]))  # []
