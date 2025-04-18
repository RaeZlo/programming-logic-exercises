"""
An ordered sequence of numbers from 1 to N is given. One number might have deleted from it, then the remaining numbers were mixed. 
Find the number that was deleted.

Example:
The starting array sequence is [1,2,3,4,5,6,7,8,9]
The mixed array with one deleted number is [3,2,4,6,7,8,1,9]
Your function should return the int 5.

If no number was deleted from the starting array, your function should return the int 0.

URL: https://www.codewars.com/kata/595aa94353e43a8746000120
"""





def find_deleted_number(arr: list[int], mixed_arr: list[int]) -> int:
    """
    Devuelve el número eliminado del array original después de ser mezclado. Si no falta ningún número, retorna 0.

    Args:
        arr (list[int]): Secuencia original ordenada.
        mixed_arr (list[int]): Secuencia mezclada con posible número eliminado.

    Returns:
        int: El número eliminado o 0 si no falta ninguno.
    """
    return sum(arr) - sum(mixed_arr)


print(find_deleted_number([1, 2, 3, 4, 5], [3, 4, 1, 5]))     # 2
print(find_deleted_number([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))  # 0
print(find_deleted_number([1], []))                          # 1
print(find_deleted_number([], []))                           # 0
