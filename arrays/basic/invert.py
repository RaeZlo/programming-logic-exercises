"""
Given a list of numbers, return their additive inverse.
Each positive number becomes negative, and each negative becomes positive.

URL: https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad
"""





def invert(numbers: list[int]) -> list[int]:
    """
    Devuelve la inversa aditiva de cada número en la lista.

    Args:
        numbers (list[int]): Lista de números enteros.

    Returns:
        list[int]: Lista con cada número invertido en signo.
    """
    return [-num for num in numbers]

print(invert([1, 2, 3, 4, 5]))    # Esperado: [-1, -2, -3, -4, -5]
print(invert([1, -2, 3, -4, 5]))  # Esperado: [-1, 2, -3, 4, -5]
print(invert([]))                 # Esperado: [] (caso borde: lista vacía)
print(invert([0, 0, 0]))          # Esperado: [0, 0, 0] (cero sigue siendo cero)
print(invert([-1, -2, -3, -4]))   # Esperado: [1, 2, 3, 4] (todos negativos se vuelven positivos)
