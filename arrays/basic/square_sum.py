"""
Complete the square sum function so that it squares each number passed into it and then 
sums the results together.

URL: https://www.codewars.com/kata/515e271a311df0350d00000f
"""





def square_sum(numbers: list[int]) -> int:
    """
    Esta función recibe una lista de números enteros y retorna la suma de sus cuadrados.

    Args:
        numbers (list[int]): Una lista con números enteros.

    Returns:
        int: La suma de los cuadrados de los números de la lista.
    """
    # Utilizamos una comprensión de lista para elevar al cuadrado cada número y luego sumarlos
    return sum(num ** 2 for num in numbers)

# Ejemplos de pruebas
print(square_sum([1, 2, 3]))      # Esperado: 14 (1^2 + 2^2 + 3^2 = 1 + 4 + 9)
print(square_sum([4, 5, 6, 7]))   # Esperado: 126 (4^2 + 5^2 + 6^2 + 7^2 = 16 + 25 + 36 + 49)
print(square_sum([10, 20, 30]))   # Esperado: 1400 (10^2 + 20^2 + 30^2 = 100 + 400 + 900)
print(square_sum([0, 0, 0, 0]))   # Esperado: 0 (0^2 + 0^2 + 0^2 + 0^2 = 0)
