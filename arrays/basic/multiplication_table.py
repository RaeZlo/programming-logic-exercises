"""
Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:
[[1,2,3],[2,4,6],[3,6,9]]

URL: https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08
"""





def multiplication_table(size:int) -> list[list[int]]:
    """
    Genera una tabla de multiplicación de tamaño `size × size`.

    Args:
        size (int): Tamaño de la tabla de multiplicación.

    Returns:
        list[list[int]]: Matriz representando la tabla de multiplicación.
    """
    table = []
    for num in range(1, size + 1):
        table.append([i * num for i in range(1, size + 1)])
    return table


print(multiplication_table(1))  # [[1]]
print(multiplication_table(2))  # [[1, 2], [2, 4]]
print(multiplication_table(3))  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
print(multiplication_table(4))  # [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
print(multiplication_table(5))  # [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], ..., [5, 10, 15, 20, 25]]
