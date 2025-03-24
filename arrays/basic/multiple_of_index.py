"""
Given an array of numbers, return a new array containing the elements that are multiples 
of their own index in the original array (indices start at 0).

URL: https://www.codewars.com/kata/5a34b80155519e1a00000009
"""





def multiple_of_index(numbers: list[int]) -> list[int]:
    """
    Filtra los números que son múltiplos de su índice en la lista.

    Args:
        numbers (list[int]): Lista de números enteros.

    Returns:
        list[int]: Lista con los números que cumplen la condición.
    """
    # Usamos una list comprehension para iterar sobre cada número y su índice en la lista.
    return [num for index, num in enumerate(numbers)  
            # Condición para incluir el número en la nueva lista:
            # 1. Si el índice es distinto de 0 y el número es múltiplo del índice.
            if (index != 0 and num % index == 0)  
            # 2. Si el índice es 0, solo incluimos el número si es 0 (para evitar errores de división por 0).
            or (index == 0 and num == 0)]

print(multiple_of_index([0, 2, 3, 6, 9, 12]))  # Esperado: [0, 2, 6, 12]
print(multiple_of_index([22, -6, 32, 82, 9, 25]))  # Esperado: [-6, 32, 9]
print(multiple_of_index([68, -1, 1, -7, 10, 10]))  # Esperado: [-1, 10]
print(multiple_of_index([0, 1, 2, 3, 4, 5]))  # Esperado: [0, 1, 2, 3, 4, 5]
print(multiple_of_index([4, 3, 2, 1]))  # Esperado: [2]
