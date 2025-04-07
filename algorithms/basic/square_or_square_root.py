"""
Write a method, that will get an integer array as parameter and will process every number from this array.
Return a new array with processing every number of the input-array like this:
If the number has an integer square root, take this, otherwise square the number.

URL: https://www.codewars.com/kata/57f6ad55cca6e045d2000627
"""





def square_or_square_root(arr: list[int]) -> list[int]:
    """
    Recorre cada número de la lista y:
    - Si tiene raíz cuadrada entera, devuelve esa raíz.
    - Si no, devuelve el número al cuadrado.

    Args:
        arr (list[int]): Lista de enteros positivos.

    Returns:
        list[int]: Lista transformada con raíces o cuadrados.
    """
    return [int(num ** 0.5) if int(num ** 0.5) ** 2 == num else num ** 2 for num in arr]


def square_or_square_root_alt(arr: list[int]) -> list[int]:
    """
    Variante usando el método `.is_integer()`:
    - Si la raíz cuadrada es un número entero, devuelve la raíz.
    - Si no, devuelve el cuadrado del número.

    Args:
        arr (list[int]): Lista de enteros positivos.

    Returns:
        list[int]: Lista transformada con raíces o cuadrados.
    """
    return [int(num ** 0.5) if (num ** 0.5).is_integer() else num ** 2 for num in arr]


print(square_or_square_root([4, 3, 9, 7, 2, 1]))      # [2, 9, 3, 49, 4, 1]
print(square_or_square_root_alt([4, 3, 9, 7, 2, 1]))  # [2, 9, 3, 49, 4, 1]
