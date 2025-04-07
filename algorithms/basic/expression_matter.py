"""
Given three integers a, b, and c, return the largest number obtained after inserting the operators +, *, and parentheses (). 
In other words, try every combination of a, b, and c with the operators, without reordering the operands, and return the maximum value.

URL: https://www.codewars.com/kata/5ae62fcf252e66d44d00008e
"""





def expression_matter(a: int, b: int, c: int) -> int:
    """
    Calcula el valor máximo posible combinando los enteros a, b y c
    usando los operadores +, * y paréntesis, sin cambiar el orden de los operandos.

    Args:
        a (int): Primer número entero.
        b (int): Segundo número entero.
        c (int): Tercer número entero.

    Returns:
        int: El valor máximo obtenido al evaluar todas las combinaciones posibles.
    """
    return max(
        a + b + c,      # Suma directa
        a * b * c,      # Multiplicación directa
        a + b * c,      # Multiplicación primero
        a * b + c,      # Multiplicación primero
        (a + b) * c,    # Suma primero, luego multiplicación
        a * (b + c)     # Suma interna primero, luego multiplicación
    )


print(expression_matter(1, 2, 3))  # 9
print(expression_matter(2, 1, 2))  # 6
print(expression_matter(1, 1, 1))  # 3
print(expression_matter(2, 2, 2))  # 8
print(expression_matter(9, 1, 1))  # 18
