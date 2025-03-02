"""
The task requires you to take a string of space-separated numbers and return a string 
containing the highest and lowest number, separated by a space. The highest number comes first.

URL: https://www.codewars.com/kata/554b4ac871d6813a03000035
"""





def high_and_low(numbers: str) -> str:
    """
    En esta función, tomamos una cadena de números separados por espacios y devolvemos una nueva cadena 
    que contiene el número más alto y el número más bajo, separados por un espacio. El número más alto 
    aparece primero.
    
    Args:
        numbers (str): Una cadena de números separados por espacios.
        
    Returns:
        str: Una cadena que contiene el número más alto y el número más bajo, separados por un espacio.
    """
    numbers = sorted([int(digit) for digit in numbers.split()])
    return f"{numbers[-1]} {numbers[0]}"

# Pruebas de la función
test1 = high_and_low("1 9 3 4 -5")
print(test1)  # Esperado: "9 -5"

test2 = high_and_low("10 20 30 40 50")
print(test2)  # Esperado: "50 10"
