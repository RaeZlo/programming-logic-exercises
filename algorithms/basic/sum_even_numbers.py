"""
Complete the function that takes a sequence of numbers as single parameter.
Your function must return the sum of the even values of this sequence.
Only numbers without decimals like 4 or 4.0 can be even.
The input is a sequence of numbers: integers and/or floats.
"""





def sum_even_numbers(seq:list[int | float]) -> int | float: 
    """
    Suma los valores pares en una secuencia de números.
    Solo considera pares aquellos números sin parte decimal que sean divisibles entre 2.

    Args:
        seq (list[float]): Lista de enteros y/o flotantes.

    Returns:
        int: Suma de los números pares sin parte decimal.
    """
    return sum(num for num in seq if num % 2 == 0)


print(sum_even_numbers([1, 2, 3, 4]))           # 6
print(sum_even_numbers([1.0, 2.0, 3.0, 4.0]))   # 6.0
print(sum_even_numbers([1.1, 2.2, 3.3]))        # 0
print(sum_even_numbers([0, -2, -4, 5]))     # -6
