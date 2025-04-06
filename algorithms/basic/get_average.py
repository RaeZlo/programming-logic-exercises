"""
It's the academic year's end, fateful moment of your school report. The averages must be calculated. 
All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.

Return the average of the given array rounded down to its nearest integer.

URL: https://www.codewars.com/kata/563e320cee5dddcf77000158
"""





def get_average(marks: list[int]) -> int:
    """
    Calcula el promedio entero (redondeado hacia abajo) de una lista de enteros.

    Args:
        marks (list[int]): Lista de enteros representando calificaciones.

    Returns:
        int: Promedio entero redondeado hacia abajo.
    """
    return sum(marks) // len(marks)


print(get_average([2, 2, 2, 2]))         # 2
print(get_average([1, 2, 3, 4, 5]))      # 3
print(get_average([5, 5, 5, 5]))         # 5
print(get_average([10, 0, 10]))          # 6
