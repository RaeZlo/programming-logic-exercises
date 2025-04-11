"""
Return an array containing the numbers from 1 to N, where N is the parametered value.

Replace certain values however if any of the following conditions are met:
If the value is a multiple of 3: use the value "Fizz" instead
If the value is a multiple of 5: use the value "Buzz" instead
If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead

URL: https://www.codewars.com/kata/5300901726d12b80e8000498
"""





def fizzbuzz(n: int) -> list:
    """
    Retorna una lista desde 1 hasta n con sustituciones según reglas FizzBuzz.

    Args:
        n (int): Límite superior de la lista.

    Returns:
        list: Lista de enteros y/o strings según las reglas de FizzBuzz.
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result


def fizzbuzz_alt(n: int) -> list:
    """
    Versión compacta de FizzBuzz utilizando expresiones booleanas.

    Args:
        n (int): Límite superior de la lista.

    Returns:
        list: Lista de enteros y/o strings según las reglas de FizzBuzz.
    """
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or i for i in range(1, n + 1)]


print(fizzbuzz(15)) # Resultado esperado: [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
