"""
We need a function that can transform a number (integer) into a string.

URL: https://www.codewars.com/kata/5265326f5fda8eb1160004c8
"""





def number_to_string(num: int) -> str:
    """
    En esta función, tomamos un número entero y lo convertimos en una cadena de texto.
    
    Args:
        num (int): El número entero que se debe convertir a cadena.
        
    Returns:
        str: El número convertido a una cadena de texto.
    """
    # f-string: f"{num}"
    # %-formatting: "%s" % num
    return str(num)

test1 = number_to_string(123)
print(test1)  # Esperado: "123"

test2 = number_to_string(-456)
print(test2)  # Esperado: "-456"
