"""
You are in a city with roads arranged in a grid. You have 10 minutes before an appointment and decide to take a walk. 
The city app gives you directions in the form of a list of one-letter strings (e.g., ['n', 's', 'w', 'e']), where each l

Your task is to check if:
The walk will take exactly 10 minutes.
You return to the starting point after the walk.
Return true if both conditions are met, otherwise return false.

URL: https://www.codewars.com/kata/54da539698b8a2ad76000228
"""





def is_valid_walk(walk: list[str]) -> bool:
    """
    Verifica si un paseo cumple con las condiciones de ser válido.

    Args:
        walk (list[str]): Lista con direcciones ('n', 's', 'e', 'w').

    Returns:
        bool: True si el paseo es válido, False en caso contrario.
    """
    # Si el paseo no dura exactamente 10 minutos, no es válido.
    if len(walk) != 10:
        return False

    # Variables para rastrear la posición en coordenadas (x, y).
    helper_y = 0  # Controla los movimientos en el eje Y.
    helper_x = 0  # Controla los movimientos en el eje X.

    # Recorremos la lista de direcciones y actualizamos las coordenadas.
    for position in walk:
        if position == "n":  # Norte (+1 en Y)
            helper_y += 1
        elif position == "s":  # Sur (-1 en Y)
            helper_y -= 1
        elif position == "e":  # Este (+1 en X)
            helper_x += 1
        elif position == "w":  # Oeste (-1 en X)
            helper_x -= 1

    # El paseo es válido si regresamos al punto de inicio (0,0).
    return helper_y == 0 and helper_x == 0


def is_valid_walk_alt(walk: list[str]) -> bool:
    """
    Alternativa más concisa usando el método count().

    Args:
        walk (list[str]): Lista con direcciones ('n', 's', 'e', 'w').

    Returns:
        bool: True si el paseo es válido, False en caso contrario.
    """
    return len(walk) == 10 and walk.count("n") == walk.count("s") and walk.count("e") == walk.count("w")



print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))  # True
print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))  # False
print(is_valid_walk(['n', 'e', 's', 'w', 'n', 'e', 's', 'w', 'n', 's']))  # False
print(is_valid_walk(['n', 'e', 'w', 's', 'n', 's', 'e', 'w', 'n', 's']))  # True
