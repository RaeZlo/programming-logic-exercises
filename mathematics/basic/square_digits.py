"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.
Happy Coding!

URL: https://www.codewars.com/kata/546e2562b03326a88e000020
"""





def square_digits(num: int) -> int:
    """
    En esta función, tomamos un número entero como argumento, luego 
    elevamos al cuadrado cada uno de sus dígitos y concatenamos los 
    resultados. Finalmente, retornamos el número resultante como entero.
    
    Args:
        num (int): El número que se va a procesar.
        
    Returns:
        int: El número formado por la concatenación de los cuadrados de 
             los dígitos del número original.
    """
    resultado = ""
    for digit in str(num):
        resultado += str(int(digit) ** 2)
    
    return int(resultado)

test1 = square_digits(9119)
print(f"El número 9119 al elevar al cuadrado sus dígitos y concatenarlos es {test1}.")  # Esperado: 811181

test2 = square_digits(765)
print(f"El número 765 al elevar al cuadrado sus dígitos y concatenarlos es {test2}.")  # Esperado: 493625
