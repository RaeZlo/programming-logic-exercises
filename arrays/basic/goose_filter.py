"""
Write a function that takes a list of strings and returns a new list with the elements that 
are not in the predefined list of geese names:
["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

The output list should maintain the same order as the input, but with the geese names removed. 
Some elements may be repeated.

URL: https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7
"""






def goose_filter(birds: list[str]) -> list[str]:
    """
    Filtra una lista de nombres de aves, eliminando los que corresponden a gansos.

    Args:
        birds (list[str]): Lista de nombres de aves.

    Returns:
        list[str]: Lista de aves sin los nombres de gansos definidos.
    """
    geese = {"African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"}  # Conjunto para búsquedas eficientes
    return [bird for bird in birds if bird not in geese]


print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Blue Swedish"]))  # Esperado: ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
print(goose_filter(["Toulouse", "Roman Tufted", "Mallard"]))  # Esperado: ["Mallard"]
print(goose_filter(["Steinbacher", "African", "Pilgrim", "Mallard", "Blue Swedish"]))  # Esperado: ["Mallard", "Blue Swedish"]
