"""
Given a random non-negative number, you have to return the digits of this number within an 
array in reverse order.

URL: https://www.codewars.com/kata/5583090cbe83f4fd8c000051
"""





def digitize(num: int) -> list[int]:
    """
    En esta función, tomamos un número entero no negativo y devolvemos una lista que contiene los dígitos 
    de este número en orden inverso.
    
    Args:
        num (int): Un número entero no negativo.
        
    Returns:
        list[int]: Una lista de los dígitos del número en orden inverso.
    """
    # Convertir el número a una cadena y luego invertirla, y finalmente convertir cada carácter de nuevo en un entero
    return [int(i) for i in str(num)[::-1]]

# Pruebas de la función
test1 = digitize(35231)
print(test1)  # Esperado: [1, 3, 2, 5, 3]

test2 = digitize(0)
print(test2)  # Esperado: [0]
