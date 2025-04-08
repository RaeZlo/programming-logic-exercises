"""
Your task is to write a function which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step.

If begin value is greater than the end, your function should return 0. If end is not the result of an integer number of steps, 
then don't add it to the sum. See the 4th example below.

URL: https://www.codewars.com/kata/586f6741c66d18c22800010a
"""





def sequence_sum(begin_number: int, end_number: int, step: int) -> int:
    """
    Retorna la suma de una secuencia de enteros definida por un valor inicial, uno final y un paso.

    Args:
        begin_number (int): Número inicial de la secuencia.
        end_number (int): Número final de la secuencia.
        step (int): Incremento entre elementos de la secuencia.

    Returns:
        int: Suma de los valores en la secuencia generada.
             Si el valor inicial es mayor que el final, retorna 0.
    """
    return sum(range(begin_number, end_number + 1, step))


print(sequence_sum(2, 6, 2))  # 2 + 4 + 6 = 12
print(sequence_sum(1, 5, 1))  # 1 + 2 + 3 + 4 + 5 = 15
print(sequence_sum(1, 5, 3))  # 1 + 4 = 5
print(sequence_sum(10, 5, 1))  # 0 (inicio mayor que fin)
