"""
Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this 
way until a single-digit number is produced. The input will be a non-negative integer.

Examples
16  -->  1 + 6 = 7

URL: https://www.codewars.com/kata/541c8630095125aba6000c00
"""





def digital_root(num: int) -> int:
    """
    En esta función, calculamos la raíz digital de un número, sumando sus dígitos de manera recursiva 
    hasta que se obtiene un único dígito.
    
    Args:
        num (int): El número del cual obtener la raíz digital.
        
    Returns:
        int: La raíz digital del número, un solo dígito.
    """
    accu = 0
    for digit in str(num):
        accu += int(digit)
    if len(str(accu)) > 1:
        accu = digital_root(accu)  # Llamada recursiva si el número tiene más de un dígito
    return accu

# Ejemplo de prueba 1
test1 = digital_root(10)
print(f"La raíz digital de 10 es: {test1}.")  # Esperado: 1

# Ejemplo de prueba 2
test2 = digital_root(16)
print(f"La raíz digital de 16 es: {test2}.")  # Esperado: 7
