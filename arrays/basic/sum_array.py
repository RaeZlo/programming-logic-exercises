"""
Write a function that takes an array of numbers and returns the sum of the numbers.
The numbers can be negative or non-integer. If the array does not contain any numbers then you 
should return 0.

Assumptions
You can assume that you are only given numbers.
You cannot assume the size of the array.
You can assume that you do get an array and if the array is empty, return 0.

URL: https://www.codewars.com/kata/53dc54212259ed3d4f00071c
"""





def sum_array(nums: list) -> int:
    """
    Esta función recibe una lista de números y retorna la suma de esos números.

    Args:
        nums (list): Una lista con números que pueden ser enteros o flotantes.

    Returns:
        int: La suma de los números de la lista, o 0 si la lista está vacía.
    """
    # Si la lista está vacía, retornamos 0, de lo contrario, sumamos los números
    return sum(nums) if nums else 0

print(sum_array([1, 2, 3]))        # Esperado: 6 (1 + 2 + 3)
print(sum_array([-1, -2, -3]))     # Esperado: -6 (-1 + -2 + -3)
print(sum_array([1.5, 2.5, 3.5]))  # Esperado: 7.5 (1.5 + 2.5 + 3.5)
print(sum_array([]))               # Esperado: 0 (La lista está vacía)
print(sum_array([0]))              # Esperado: 0 (Solo hay un 0)
