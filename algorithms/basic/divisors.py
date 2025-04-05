"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's 
divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime'

URL: https://www.codewars.com/kata/544aed4c4a30184e960010f4
"""





def divisors(integer: int) -> list[int] | str:
    """
    Devuelve los divisores propios del número entero dado (excluyendo 1 y él mismo).
    Si el número es primo, retorna un mensaje indicándolo.

    Args:
        integer (int): Número entero mayor que 1.

    Returns:
        list[int] | str: Lista de divisores o un string si es primo.
    """
    helper = []
    for num in range(2, integer):
        if integer % num == 0:
            helper.append(num)
    
    return f"{integer} is prime" if not helper else helper


print(divisors(15))   # [3, 5]
print(divisors(12))   # [2, 3, 4, 6]
print(divisors(13))   # "13 is prime"
print(divisors(28))   # [2, 4, 7, 14]
