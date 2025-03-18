"""
In this simple exercise, you will write a function that takes two integers; n and limit; 
and returns a list of the multiples of n up to and possibly including limit.
It is guaranteed that n > 0 and limit >= n.

URL: https://www.codewars.com/kata/58ca658cc0d6401f2700045f
"""





def find_multiples(num:int, limit:int) -> list[int]:
    """
    Encuentra los múltiplos de un número hasta un límite dado.

    Args:
        num (int): Número base cuyos múltiplos se buscan.
        limit (int): Límite superior hasta el cual se buscarán los múltiplos.

    Returns:
        list[int]: Lista de múltiplos de 'num' hasta 'limit'.
    """
    return list(range(num, limit + 1, num))

print(find_multiples(2, 10))   # Esperado: [2, 4, 6, 8, 10]
print(find_multiples(3, 15))   # Esperado: [3, 6, 9, 12, 15]
print(find_multiples(5, 25))   # Esperado: [5, 10, 15, 20, 25]
print(find_multiples(7, 30))   # Esperado: [7, 14, 21, 28]
