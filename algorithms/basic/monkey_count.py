"""
You take your son to the forest to see the monkeys. You know that there are a certain number there (n), but your son is too young 
to just appreciate the full number, he has to start counting them from 1.
As a good parent, you will sit and count with him. Given the number (n), populate an array with all numbers up to 
and including that number, but excluding zero.

URL: https://www.codewars.com/kata/56f69d9f9400f508fb000ba7
"""






def monkey_count(n:int) -> list[int]:
    """
    Genera una lista con los números del 1 hasta n (inclusive).

    Args:
        n (int): Número entero positivo.

    Returns:
        list[int]: Lista de enteros desde 1 hasta n.
    """
    return list(range(1, n + 1))


print(monkey_count(5))   # [1, 2, 3, 4, 5]
print(monkey_count(1))   # [1]
print(monkey_count(10))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
