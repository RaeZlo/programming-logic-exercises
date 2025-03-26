"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those 
numbers in the form of a phone number.
Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

URL: https://www.codewars.com/kata/525f50e3b73515a6db000b83
"""






def create_phone_number(phone_number: list[int]) -> str:
    """
    Convierte una lista de 10 números enteros en un formato de número de teléfono.

    Args:
        phone_number (list[int]): Lista de 10 dígitos enteros entre 0 y 9.

    Returns:
        str: Número de teléfono formateado como "(XXX) XXX-XXXX".
    """
    # Verifica que todos los números están en el rango 0-9
    if all(0 <= num <= 9 for num in phone_number) and len(phone_number) == 10:
        # Usa format() con * para desempaquetar la lista e insertarlos en la cadena
        return "({}{}{}) {}{}{}-{}{}{}{}".format(*phone_number)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # "(123) 456-7890"
print(create_phone_number([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))  # "(987) 654-3210"
print(create_phone_number([5, 5, 5, 1, 2, 3, 4, 5, 6, 7]))  # "(555) 123-4567"
