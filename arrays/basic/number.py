"""
Write a function which takes a list of strings and returns each line prepended by the correct number.
The numbering starts at 1. The format is n: string. Notice the colon and space in between.

URL: https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9
"""





def number(lines: list[str]) -> list[str]:
    """
    Esta función recibe una lista de cadenas y devuelve una nueva lista donde cada línea
    está precedida por su número de línea, comenzando desde 1.

    Args:
        lines (list[str]): Lista de líneas de texto.

    Returns:
        list[str]: Lista con las líneas numeradas en el formato 'n: string'.
    """
    return [f"{i}: {line}" for i, line in enumerate(lines, start=1)]


# Ejemplos de pruebas
print(number(["a", "b", "c"]))  # Esperado: ['1: a', '2: b', '3: c']
print(number([]))               # Esperado: [] (caso borde con lista vacía)
print(number(["Hola"]))         # Esperado: ['1: Hola'] (caso borde con una sola línea)
print(number(["Uno", "Dos", "Tres", "Cuatro"]))  # Esperado: ['1: Uno', '2: Dos', '3: Tres', '4: Cuatro']
