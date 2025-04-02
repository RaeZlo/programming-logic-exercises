"""
Complete the method which returns the number which is most frequent in the given input array. 
If there is a tie for most frequent number, return the largest number among them.

URL: https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004
"""





def highest_rank(arr:list[int]) -> int:
    helper = {}
    for num in arr:
        # Si el número no está en el diccionario, lo agregamos
        # La clave es el número, y el valor es una tupla: (frecuencia, número)
        if num not in helper:
            # Contamos cuántas veces aparece 'num' en la lista 'arr' usando arr.count(num)
            # Guardamos en el diccionario la tupla (frecuencia, número)
            helper[num] = arr.count(num), num
    
    # Usamos max() para encontrar el elemento con la mayor frecuencia
    # max() comparará las tuplas (frecuencia, número) y devolverá la tupla con la mayor frecuencia
    # Luego, accedemos a [1] para obtener solo el número (el segundo valor de la tupla)
    return max(helper.values())[1]


def highest_rank_alt(arr: list[int]) -> int:
    """
    Alternativa usando sorted() y max() con key=arr.count.

    Args:
        arr (list[int]): Lista de enteros.

    Returns:
        int: El número más frecuente (o el más grande en caso de empate).
    """
    # Ordenamos la lista en orden descendente y usamos max() con arr.count como criterio
    return max(sorted(arr, reverse=True), key=arr.count)



print(highest_rank([1, 2, 3, 3, 2, 1, 2]))  # 2
print(highest_rank([4, 4, 2, 2, 5, 5]))     # 5
print(highest_rank([10, 20, 30, 10, 30, 30]))  # 30
print(highest_rank([1]))                   # 1
print(highest_rank([5, 5, 5, 5, 1, 2, 2]))  # 5
