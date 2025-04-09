"""
Given a non-negative integer b, write a function which returns an integer d such that the binary 
representation of b is the same as the decimal representation of d.

URL: https://www.codewars.com/kata/59fca81a5712f9fa4700159a
"""





def to_binary(n:int) -> int:
    """
    Convierte un número entero no negativo a su representación binaria, pero retorna el resultado como entero decimal.

    Args:
        n (int): Número entero no negativo.

    Returns:
        int: Representación binaria de n, interpretada como número decimal.
            Por ejemplo, si n = 5 → binario = '101' → retorna 101 como int.
    """
    return int(bin(n)[2:])


print(to_binary(1))   # 1
print(to_binary(5))   # 101
print(to_binary(10))  # 1010
print(to_binary(0))   # 0
