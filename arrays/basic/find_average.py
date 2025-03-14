"""
Write a function which calculates the average of the numbers in a given array.

URL: https://www.codewars.com/kata/57a2013acf1fa5bfc4000921
"""





def find_average(numbers: list[float]) -> float:
    """
    Esta función recibe una lista de números y retorna su promedio.
    
    Args:
        numbers (list[float]): Una lista con números reales (positivos o negativos).
        
    Returns:
        float: El promedio de los números de la lista. Si la lista está vacía, retorna 0.
    """
    # Si la lista está vacía, devolvemos 0, de lo contrario, calculamos el promedio
    return 0 if not numbers else sum(numbers) / len(numbers)

print(find_average([1, 2, 3, 4, 5]))  # Esperado: 3.0 (promedio de los números)
print(find_average([10, 20, 30]))     # Esperado: 20.0 (promedio de los números)
print(find_average([7, 5, 9]))        # Esperado: 7.0 (promedio de los números)
print(find_average([]))               # Esperado: 0 (lista vacía)
