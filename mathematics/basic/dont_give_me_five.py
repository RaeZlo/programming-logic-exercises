"""
You are given two numbers: a start number and an end number (both inclusive). 
You need to count all the numbers between the start and end, excluding those that contain the digit 5.

URL: https://www.codewars.com/kata/5813d19765d81c592200001a
"""





def dont_give_me_five(start, end):
    """
    En esta función, contamos todos los números entre `start` y `end` (ambos incluidos) 
    que no contienen el dígito '5'. Si un número contiene el dígito '5', se excluye de la cuenta.
    
    Args:
        start (int): El número de inicio del rango.
        end (int): El número de fin del rango.
        
    Returns:
        int: El número de números en el rango que no contienen el dígito '5'.
    """
    return len([1 for i in range(start, end + 1) if '5' not in str(i)])

test1 = dont_give_me_five(1, 10)
print(f"La cantidad de números que no contiene 5 es: {test1}")  # Esperado: 9

test2 = dont_give_me_five(1, 20)
print(f"La cantidad de números que no contiene 5 es: {test2}")  # Esperado: 18
