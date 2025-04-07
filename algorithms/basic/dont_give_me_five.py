"""
In this kata you get the start number and the end number of a region and should return the count of all numbers 
except numbers with a 5 in it. The start and the end number are both inclusive!
The result may contain fives. ;-)
The start number will always be smaller than the end number. Both numbers can be also negative!

URL: https://www.codewars.com/kata/5813d19765d81c592200001a
"""





def dont_give_me_five(start: int, end: int) -> int:
    """
    Cuenta los números en el rango dado que no contienen el dígito 5.

    Args:
        start (int): Número inicial del rango (inclusive).
        end (int): Número final del rango (inclusive).

    Returns:
        int: Cantidad de números que no contienen el dígito 5.
    """
    return len([num for num in range(start, end + 1) if "5" not in str(num)])


print(dont_give_me_five(1, 9))       # 8 (solo el 5 queda fuera)
print(dont_give_me_five(4, 17))      # 12
print(dont_give_me_five(-10, 10))    # 19 (excluye -5 y 5)
