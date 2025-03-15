"""
You take your son to the forest to see the monkeys. You know that there are a certain number there (n),
but your son is too young to just appreciate the full number, he has to start counting them from 1.

As a good parent, you will sit and count with him. Given the number (n), populate an array with all 
numbers up to and including that number, but excluding zero.

URL: https://www.codewars.com/kata/56f69d9f9400f508fb000ba7
"""





def monkey_count(num: int) -> list[int]:
    """
    Esta función recibe un número entero positivo y retorna una lista con los números del 1 hasta n.

    Args:
        num (int): Un número entero positivo.

    Returns:
        list[int]: Una lista con los números del 1 hasta n.
    """
    return list(range(1, num + 1))  # Convertimos el rango en una lista

print(monkey_count(5))   # Esperado: [1, 2, 3, 4, 5]
print(monkey_count(10))  # Esperado: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(monkey_count(1))   # Esperado: [1] (caso borde con el número más pequeño posible)
print(monkey_count(0))   # Esperado: [] (caso borde con cero)
print(monkey_count(15))  # Esperado: [1, 2, 3, ..., 15]
