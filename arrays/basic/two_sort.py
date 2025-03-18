"""
You will be given a list of strings. You must sort it alphabetically 
(case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.
You should not remove or add elements from/to the array.

URL: https://www.codewars.com/kata/57cfdf34902f6ba3d300001e
"""






def two_sort(array: list[str]) -> str:
    """
    Ordena la lista alfabéticamente y devuelve la primera palabra con '***' entre sus letras.

    Args:
        array (list[str]): Lista de strings.

    Returns:
        str: Primer string en orden alfabético con '***' como separador entre letras.
    """
    # Se ordena la lista alfabéticamente respetando la sensibilidad de mayúsculas y minúsculas
    sorted_array = sorted(array)
    
    # Se toma el primer elemento de la lista ordenada y se separan sus caracteres con '***'
    return "***".join(sorted_array[0])

print(two_sort(["bitcoin", "take", "over", "the", "world"]))  # Esperado: "b***i***t***c***o***i***n"
print(two_sort(["apple", "Banana", "cherry", "date"]))       
print(two_sort(["zebra", "alpha", "omega"]))               
print(two_sort(["Hello", "hello", "HELLO"]))       
