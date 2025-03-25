"""
Your task is to sum the differences between consecutive pairs in the array in descending order.

URL: https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e
"""





def sum_of_differences(arr: list[int]) -> int:
    """
    Calcula la suma de las diferencias entre pares consecutivos en el array ordenado de mayor a menor.

    Args:
        arr (list[int]): Lista de números enteros.

    Returns:
        int: La suma de las diferencias entre pares consecutivos.
    """
    if len(arr) < 2:
        return 0  # Si hay menos de 2 elementos, no hay diferencias que calcular

    arr.sort(reverse=True)  # Ordenamos el array en orden descendente
    return sum(arr[i] - arr[i + 1] for i in range(len(arr) - 1))  # Calculamos la suma de diferencias


print(sum_of_differences([2, 1, 10]))  # Esperado: 9 (10-2)
print(sum_of_differences([5, 3, 8, 1]))  # Esperado: 7 (8-5 + 5-3 + 3-1)
print(sum_of_differences([1]))  # Esperado: 0 (No hay diferencias)
print(sum_of_differences([]))  # Esperado: 0 (Lista vacía)
print(sum_of_differences([10, 10, 10]))  # Esperado: 0 (Las diferencias son 0)
