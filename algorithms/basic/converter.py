"""
Create an application that will display the number of kilometers per liter (output) based on the 
number of miles per imperial gallon (input).
Make sure to round off the result to two decimal points.

Some useful associations relevant to this kata:
1 Imperial Gallon = 4.54609188 litres
1 Mile = 1.609344 kilometres

URL: https://www.codewars.com/kata/557b5e0bddf29d861400005d
"""





def converter(mpg: int) -> float:
    """
    Convierte millas por galón imperial a kilómetros por litro.

    Args:
        mpg (int): Millas por galón imperial.

    Returns:
        float: Kilómetros por litro, redondeado a dos decimales.
    """
    return round(mpg * (1.609344 / 4.54609188), 2)


print(converter(10))    # 3.54
print(converter(20))    # 7.08
print(converter(30))    # 10.62
print(converter(0))     # 0.0
