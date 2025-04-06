"""
You are given an odd-length array of integers, in which all of them are the same, except for one single number.
Complete the method which accepts such an array, and returns that single different number.

URL: https://www.codewars.com/kata/57f609022f4d534f05000024
"""






def stray(arr: list[int]) -> int:
    """
    Devuelve el número único en una lista donde todos los elementos son iguales excepto uno.

    Args:
        arr (list[int]): Lista de enteros con longitud impar.

    Returns:
        int: El único número diferente en la lista.
    """
    for i in set(arr):
        if arr.count(i) == 1:
            return i


def stray_alt(arr: list[int]) -> int:
    """
    Alternativa con min() y key para encontrar el número único en la lista.

    Args:
        arr (list[int]): Lista de enteros con longitud impar.

    Returns:
        int: El único número diferente en la lista.
    """
    return min(arr, key=arr.count)


print(stray([1, 1, 2]))             # 2
print(stray([17, 17, 3, 17, 17]))   # 3
print(stray_alt([7, 7, 0, 7]))      # 0
