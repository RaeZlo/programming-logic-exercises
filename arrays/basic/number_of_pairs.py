"""
Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number 
of pair of gloves you can constitute from the gloves you have in your drawer.
Given an array describing the color of each glove, return the number of pairs you can constitute, assuming that 
only gloves of the same color can form pairs.

Examples:
input = ["red", "green", "red", "blue", "blue"]
result = 2 (1 red pair + 1 blue pair)

URL: https://www.codewars.com/kata/58235a167a8cb37e1a0000db
"""





def number_of_pairs(gloves: list[str]) -> int:
    """
    Cuenta cuántos pares de guantes pueden formarse.

    Args:
        gloves (list[str]): Lista de colores de guantes.

    Returns:
        int: Número de pares que pueden formarse.
    """
    helper = {}
    # Contamos la cantidad de cada color
    for glove in gloves:
        if glove in helper:
            helper[glove] += 1
        else:
            helper[glove] = 1
    # Sumamos los pares (división entera por 2)
    pairs = 0
    for count in helper.values():
        pairs += count // 2

    return pairs


def number_of_pairs_alt(gloves: list[str]) -> int:
    """
    Variante con menor código.
    """
    return sum(gloves.count(color) // 2 for color in set(gloves))



print(number_of_pairs(["red", "green", "red", "blue", "blue"]))  # 2 (rojo + azul)
print(number_of_pairs(["red", "red", "red", "red", "red"]))  # 2 (dos pares rojos)
print(number_of_pairs(["blue", "blue", "green", "green", "green", "green"]))  # 3 (dos verdes + un azul)
print(number_of_pairs(["yellow"]))  # 0 (sin pares)
print(number_of_pairs([]))  # 0 (lista vacía)
