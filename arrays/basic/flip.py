"""
Bob has a box with columns of toy cubes. Each column has a certain number of cubes. 
The gravity in the box can change direction and pull the cubes either to the left ('L') or to the right ('R').

Your task is to find out how the cubes will be arranged after the gravity switches. 
After switching, the cubes will rearrange in ascending order, either from left to right or right to left, 
depending on the direction of the gravity.

Example:
'R', [3, 2, 1, 2] -> [1, 2, 2, 3]
'L', [1, 4, 5, 3, 5] -> [5, 5, 4, 3, 1]

URL: https://www.codewars.com/kata/5f70c883e10f9e0001c89673
"""





def flip(direction: str, cube: list[int]) -> list[int]:
    """
    Ordena los cubos según la dirección de la gravedad.

    Args:
        direction (str): Dirección de la gravedad ('L' para izquierda, 'R' para derecha).
        cube (list[int]): Lista con las alturas de las columnas de cubos.

    Returns:
        list[int]: Lista de cubos ordenada según la gravedad.
    """
    return sorted(cube, reverse=True) if direction == "L" else sorted(cube)

print(flip("R", [3, 2, 1, 2]))  # Esperado: [1, 2, 2, 3]
print(flip("L", [1, 4, 5, 3, 5]))  # Esperado: [5, 5, 4, 3, 1]
print(flip("R", [5, 7, 2, 4, 8]))  # Esperado: [2, 4, 5, 7, 8]
print(flip("L", [1, 2, 3, 4, 5]))  # Esperado: [5, 4, 3, 2, 1]
