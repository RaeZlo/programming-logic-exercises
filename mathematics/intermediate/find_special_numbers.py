"""
The number 89 is the first integer with more than one digit that satisfies a special property. 
It can be written as the sum of each of its digits raised to the power of their respective positions:
89 = 8^1 + 9^2

Another number with this property is 135:
135 = 1^1 + 3^2 + 5^3

Task:
Write a function that takes two integers, a and b, defining a range [a, b] (inclusive), and returns a list 
of numbers in this range that satisfy the described property.

URL: https://www.codewars.com/kata/5626b561280a42ecc50000d1
"""





def find_special_numbers(a, b):
    """
    Esta función recibe dos números enteros, a y b, y retorna una lista de números en el rango [a, b] 
    que cumplen la propiedad especial descrita: la suma de cada uno de sus dígitos elevados a la potencia 
    de sus posiciones respectivas es igual al propio número.
    
    Args:
        a (int): El número inicial del rango.
        b (int): El número final del rango.
        
    Returns:
        list: Una lista con los números en el rango [a, b] que cumplen la propiedad.
    """
    special_numbers = []
    
    for num in range(a, b + 1):
        digits = str(num)  
        total_sum = sum(int(digit) ** (i + 1) for i, digit in enumerate(digits)) 
        
        if total_sum == num:
            special_numbers.append(num)
    
    return special_numbers

test1 = find_special_numbers(1, 100)
print(f"Los números especiales son: {test1}") # Esperado: [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

test2 = find_special_numbers(90, 100)
print(f"Los números especiales son: {test2}") # Esperado: []
