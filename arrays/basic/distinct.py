"""
Define a function that removes duplicates from an array of non-negative numbers 
and returns it as a result. The order of the sequence has to stay the same.

URL: https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118
"""





def distinct(seq: list[int]) -> list[int]:
    """
    Elimina los elementos duplicados de la lista sin alterar el orden.

    Args:
        seq (list[int]): Lista de números no negativos.

    Returns:
        list[int]: Lista sin duplicados, manteniendo el orden original.
    """
    result = []
    for num in seq:
        if num not in result:
            result.append(num)
    
    return result


def distinct_alt(seq: list[int]) -> list[int]:
    """
    Elimina los elementos duplicados usando un conjunto y devuelve una lista ordenada.

    Args:
        seq (list[int]): Lista de números no negativos.

    Returns:
        list[int]: Lista sin duplicados, ordenada de menor a mayor.
    """
    return sorted(set(seq))


print(distinct([1, 2, 2, 3, 4, 4, 5]))   # Esperado: [1, 2, 3, 4, 5]
print(distinct([7, 7, 6, 6, 5, 5]))      # Esperado: [7, 6, 5]
print(distinct([10, 20, 10, 30]))        # Esperado: [10, 20, 30]

print(distinct_alt([1, 2, 2, 3, 4, 4, 5]))   # Esperado: [1, 2, 3, 4, 5]
print(distinct_alt([7, 7, 6, 6, 5, 5]))      # Esperado: [5, 6, 7]
print(distinct_alt([10, 20, 10, 30]))        # Esperado: [10, 20, 30]
