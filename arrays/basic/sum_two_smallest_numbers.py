"""
Create a function that returns the sum of the two lowest positive numbers given an array of 
minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

URL: https://www.codewars.com/kata/558fc85d8fd1938afb000014
"""





def sum_two_smallest_numbers(numbers: list[int]) -> int:
    """
    Esta función recibe una lista de números positivos y retorna la suma de los dos números más pequeños.

    Args:
        numbers (list[int]): Una lista con al menos 4 números enteros positivos.
        
    Returns:
        int: La suma de los dos números más pequeños.
    """
    # Ordenamos la lista y sumamos los dos primeros números
    numbers = sorted(numbers)
    return numbers[0] + numbers[1]

def sum_two_smallest_numbers_alt(numbers: list[int]) -> int:
    """
    Función alternativa para obtener la suma de los dos números más pequeños de una lista.
    
    Args:
        numbers (list[int]): Una lista con al menos 4 números enteros positivos.
        
    Returns:
        int: La suma de los dos números más pequeños.
    """
    # Alternativa utilizando la función sum y slicing
    return sum(sorted(numbers)[:2])

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))  # Esperado: 7 (2 + 5)
print(sum_two_smallest_numbers([10, 15, 3, 7]))      # Esperado: 10 (3 + 7)

print(sum_two_smallest_numbers_alt([19, 5, 42, 2, 77]))  # Esperado: 7 (2 + 5)
print(sum_two_smallest_numbers_alt([10, 15, 3, 7]))      # Esperado: 10 (3 + 7)
