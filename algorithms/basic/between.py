"""
Complete the function that takes two integers (a, b, where a < b) and return an array of all 
integers between the input parameters, including them.

URL: https://www.codewars.com/kata/55ecd718f46fba02e5000029
"""





def between(a: int, b: int) -> list[int]:
    """
    Retorna una lista con todos los enteros entre `a` y `b`, incluyendo ambos.

    Args:
        a (int): Límite inferior del rango.
        b (int): Límite superior del rango.

    Returns:
        list[int]: Lista de enteros desde a hasta b (inclusive).
    """
    return list(range(a, b + 1))


print(between(1, 4))  # [1, 2, 3, 4]
print(between(-2, 2)) # [-2, -1, 0, 1, 2]
