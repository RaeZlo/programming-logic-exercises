"""
Your task is to split the chocolate bar of given dimension n x m into small squares. Each square is of size 1x1 and unbreakable. 
Implement a function that will return minimum number of breaks needed.

For example if you are given a chocolate bar of size 2 x 1 you can split it to single squares in just one break, 
but for size 3 x 1 you must do two breaks.

If input data is invalid you should return 0 (as in no breaks are needed if we do not have any chocolate to split). 
Input will always be a non-negative integer.

URL: https://www.codewars.com/kata/534ea96ebb17181947000ada
"""





def break_chocolate(n: int, m: int) -> int:
    """
    Calcula el número mínimo de cortes necesarios para dividir una barra de chocolate
    de tamaño n x m en cuadrados individuales de 1x1.

    Args:
        n (int): Número de filas.
        m (int): Número de columnas.

    Returns:
        int: Número mínimo de cortes necesarios. Si alguna dimensión es 0, retorna 0.
    """
    if n == 0 or m == 0:
        return 0
    return n * m - 1


def break_chocolate_alt(n: int, m: int) -> int:
    """
    Versión alternativa que retorna directamente el máximo entre (n*m - 1) y 0,
    evitando condicionales explícitos.

    Args:
        n (int): Número de filas.
        m (int): Número de columnas.

    Returns:
        int: Número mínimo de cortes necesarios o 0 si alguna dimensión es 0.
    """
    return max(n * m - 1, 0)


print(break_chocolate(5, 5))   # 24
print(break_chocolate(2, 1))   # 1
print(break_chocolate(1, 1))   # 0
print(break_chocolate(0, 5))   # 0
print(break_chocolate(3, 0))   # 0
