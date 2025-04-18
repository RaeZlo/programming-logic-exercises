"""
Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.

For example n = 3 result in:
"I\n I\n  I"

URL: https://www.codewars.com/kata/5b4e779c578c6a898e0005c5
"""





def draw_stairs(n: int) -> str:
    """
    Dibuja una escalera con 'I' en n niveles, desplazando cada línea un espacio más a la derecha.

    Args:
        n (int): Número de niveles de la escalera.

    Returns:
        str: Escalera representada como un string con saltos de línea.
    """
    return "\n".join(" " * i + "I" for i in range(n))


print(draw_stairs(1))
# I

print(draw_stairs(3))
# I
#  I
#   I

print(draw_stairs(5))
# I
#  I
#   I
#    I
#     I
