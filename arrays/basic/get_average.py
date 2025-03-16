"""
Calculate the average of an array of integers, rounding down to the nearest integer.

URL: https://www.codewars.com/kata/563e320cee5dddcf77000158
"""





def get_average(marks: list[int]) -> int:
    """
    Calcula el promedio de una lista de calificaciones y lo redondea hacia abajo.

    Args:
        marks (list[int]): Lista de calificaciones como números enteros.

    Returns:
        int: Promedio redondeado hacia abajo.
    """
    return sum(marks) // len(marks)

print(get_average([2, 2, 2, 2]))  # Esperado: 2 ((2+2+2+2)/4 = 2)
print(get_average([1, 5, 87, 45, 8, 8]))  # Esperado: 25 ((1+5+87+45+8+8)/6 = 25.666 -> 25)
print(get_average([90, 80, 70, 60, 50]))  # Esperado: 70 ((90+80+70+60+50)/5 = 70)
print(get_average([100, 100, 99, 98]))  # Esperado: 99 ((100+100+99+98)/4 = 99.25 -> 99)
