"""
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of 
those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!

URL: https://www.codewars.com/kata/525f50e3b73515a6db000b83
"""





def create_phone_number(phone_number: list[int]) -> str:
    """
    Esta función recibe una lista de 10 números enteros (entre 0 y 9) y devuelve una cadena de texto que 
    representa un número de teléfono en el formato estándar (XXX) XXX-XXXX.

    Args:
        phone_number (list[int]): Lista de 10 enteros representando un número de teléfono.

    Returns:
        str: Número de teléfono formateado en el formato "(XXX) XXX-XXXX".
    """
    # Verificamos si la longitud de la lista es 10.
    if len(phone_number) == 10:
        # Usamos la función `format` para insertar los números en el formato deseado.
        return "({}{}{}) {}{}{}-{}{}{}{}".format(*phone_number)
    # Si la lista no tiene 10 elementos, retornamos una cadena vacía (aunque no debería ser necesario con datos válidos).
    return "Please provide a valid phone number"


# Pruebas de ejemplo
test1 = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(f"Resultado de la prueba 1: {test1}")  # Esperado: "(123) 456-7890"

test2 = create_phone_number([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
print(f"Resultado de la prueba 2: {test2}")  # Esperado: "(987) 654-3210"

test3 = create_phone_number([5, 5, 5, 1, 2, 3, 4, 5, 6, 7])
print(f"Resultado de la prueba 3: {test3}")  # Esperado: "(555) 123-4567"
