"""
Given a list of integers, determine whether the sum of its elements is odd or even.
Give your answer as a string matching "odd" or "even".
If the input array is empty consider it as: [0] (array with a zero).

URL: https://www.codewars.com/kata/5949481f86420f59480000e7
"""





def odd_or_even(numbers: list[int]) -> str:
    """
    Esta función recibe una lista de enteros y determina si la suma de sus elementos es par o impar.
    
    Args:
        numbers (list[int]): Una lista con enteros, que puede estar vacía.
        
    Returns:
        str: "even" si la suma es par, "odd" si la suma es impar.
    """
    # Si la lista está vacía, se considera como [0], por lo tanto, la suma es 0 (par)
    return "even" if sum(numbers) % 2 == 0 else "odd"

print(odd_or_even([1, 2, 3, 4]))       # Esperado: "even" (1+2+3+4 = 10, par)
print(odd_or_even([1, 2, 3]))          # Esperado: "even" (1+2+3 = 6, par)
print(odd_or_even([1, 3, 5]))          # Esperado: "odd" (1+3+5 = 9, impar)
print(odd_or_even([]))                 # Esperado: "even" (la lista vacía se considera [0], par)
