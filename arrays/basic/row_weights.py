"""
Given an array of positive numbers representing the weights of people in a row, divide them into two teams alternately 
(the first person goes to team 1, the second to team 2, the third to team 1, and so on). 
Return an array or tuple with the total weight of each team.

URL: https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9
"""





def row_weights(weights: list[int]) -> tuple[int, int]:
    """
    Calcula el peso total de cada equipo dividiendo las personas en dos grupos alternados.

    Args:
        weights (list[int]): Lista de pesos de las personas.

    Returns:
        tuple[int, int]: Tupla con el peso total de cada equipo.
    """
    team_1 = 0  # Suma de pesos del equipo 1
    team_2 = 0  # Suma de pesos del equipo 2

    # Recorremos la lista y asignamos el peso a uno de los equipos según el índice
    for index, weight in enumerate(weights):
        if index % 2 == 0:  # Índices pares → equipo 1
            team_1 += weight
        else:  # Índices impares → equipo 2
            team_2 += weight

    return (team_1, team_2)


def row_weights_alt(weights: list[int]) -> tuple[int, int]:
    """
    Versión alternativa usando slicing para obtener los valores alternados.

    Args:
        weights (list[int]): Lista de pesos de las personas.

    Returns:
        tuple[int, int]: Tupla con el peso total de cada equipo.
    """
    return sum(weights[::2]), sum(weights[1::2])


print(row_weights([50, 60, 70, 80]))  # Esperado: (120, 140)
print(row_weights([80]))  # Esperado: (80, 0)
print(row_weights([100, 50]))  # Esperado: (100, 50)
print(row_weights([13, 27, 49]))  # Esperado: (62, 27)
print(row_weights([70, 58, 75, 34, 91]))  # Esperado: (236, 92)
