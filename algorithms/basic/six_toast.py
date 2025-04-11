"""
You want to make 6 pieces of toast, but you're not sure how many you've already put in the toaster. 
You need to figure out how many more (or fewer) pieces you need to make it exactly 6. The result will 
always be a positive number, never negative.

Examples:
If you have 5 toasts, you need to put 1 more.
If you have 12 toasts, you need to remove 6.

Return the number of toasts you need to add or remove to make it exactly 6.

URL: https://www.codewars.com/kata/5834fec22fb0ba7d080000e8
"""





def six_toast(num: int) -> int:
    """
    Calcula cuántas tostadas se deben añadir o quitar para tener exactamente 6.

    Args:
        num (int): Número actual de tostadas.

    Returns:
        int: Diferencia absoluta respecto a 6.
    """
    return abs(6 - num)


print(six_toast(5))   # Esperado: 1
print(six_toast(12))  # Esperado: 6
print(six_toast(6))   # Esperado: 0
