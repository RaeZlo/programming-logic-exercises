"""
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels.
The input string will only consist of lower case letters and/or spaces.

URL: https://www.codewars.com/kata/54ff3102c1bad923760001f3
"""





def get_count_vowel(sentence:str) -> int:
    """
    Esta función recibe una cadena de texto y cuenta cuántas vocales (a, e, i, o, u) contiene.
    
    Args:
        sentence (str): La cadena de texto en la que se contarán las vocales.
        
    Returns:
        int: El número de vocales en la cadena.
    """
    return sum(1 for char in sentence if char in 'AEIOUaeiou')

test1 = get_count_vowel("PEdro es raro.")
print(f"El número de vocales es: {test1}") # Esperado: 5

test2 = get_count_vowel("hola mundo")
print(f"El número de vocales es: {test2}")  # Esperado: 4
