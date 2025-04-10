"""
In this kata you should simply determine, whether a given year is a leap year or not. 

In case you don't know the rules, here they are:
Years divisible by 4 are leap years,
but years divisible by 100 are not leap years,
but years divisible by 400 are leap years.

URL: https://www.codewars.com/kata/526c7363236867513f0005ca
"""





def is_leap_year(year: int) -> bool:
    """
    Determina si un año es bisiesto según las reglas del calendario gregoriano.

    Args:
        year (int): Año a evaluar.

    Returns:
        bool: True si el año es bisiesto, False si no lo es.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(is_leap_year(2020))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(2023))  # False
