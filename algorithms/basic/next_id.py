"""
You've got much data to manage and of course you use zero-based and non-negative ID's to make each data item unique!
Therefore you need a method, which returns the smallest unused ID for your next new data item...
Note: The given array of used IDs may be unsorted. For test reasons there may be duplicate IDs, but you don't have to find or remove them!

URL: https://www.codewars.com/kata/55eea63119278d571d00006a
"""





def next_id(ids: list[int]) -> int:
    """
    Encuentra el ID más pequeño no utilizado en una lista de IDs no negativos.

    Args:
        ids (list[int]): Lista de IDs utilizados (puede contener duplicados y estar desordenada).

    Returns:
        int: El ID más pequeño disponible.
    """
    for i in range(len(ids) + 1):
        if i not in ids:
            return i


print(next_id([0, 1, 2, 3, 5]))        # 4
print(next_id([0, 1, 2, 3, 4]))        # 5
print(next_id([5, 3, 0, 1, 2]))        # 4
print(next_id([]))                    # 0
print(next_id([0, 1, 1, 2, 3, 3, 5]))  # 4
