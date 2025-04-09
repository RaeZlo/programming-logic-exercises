"""
Implement the function generateRange which takes three arguments (start, stop, step) and returns the range of integers 
from start to stop (inclusive) in increments of step.

URL: https://www.codewars.com/kata/55eca815d0d20962e1000106
"""





def generate_range(start: int, stop: int, step: int) -> list[int]:
    """
    Genera una lista de enteros desde `start` hasta `stop` (ambos inclusive), en incrementos de `step`.

    Args:
        start (int): Valor inicial de la secuencia.
        stop (int): Valor final de la secuencia (inclusive).
        step (int): Incremento entre valores sucesivos.

    Returns:
        list[int]: Lista de enteros generada desde `start` hasta `stop`, con pasos de `step`.
    """
    return list(range(start, stop + 1, step))


print(generate_range(2, 10, 2))   # [2, 4, 6, 8, 10]
print(generate_range(1, 5, 1))    # [1, 2, 3, 4, 5]
print(generate_range(0, 20, 5))   # [0, 5, 10, 15, 20]
