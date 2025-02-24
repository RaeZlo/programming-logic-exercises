"""
Create a function that takes an integer as an argument and returns "Even" for even numbers 
or "Odd" for odd numbers.

URL: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/
"""





def even_or_odd(num: int) -> str:
    """
    Esta función toma un número entero como argumento y retorna "Even" 
    si el número es par, o "Odd" si el número es impar.
    
    Args:
        num (int): El número a evaluar.
        
    Returns:
        str: "Even" si el número es par, "Odd" si el número es impar.
    """
    return "Even" if num % 2 == 0 else "Odd"

test1 = even_or_odd(2)
print(f"El número 2 es {test1}.")  # Esperado: Even

test2 = even_or_odd(7)
print(f"El número 7 es {test2}.")  # Esperado: Odd
