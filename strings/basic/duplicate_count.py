"""
Write a function that will return the count of distinct case-insensitive alphabetic characters 
and numeric digits that occur more than once in the input string. The input string can be assumed 
to contain only alphabets (both uppercase and lowercase) and numeric digits.

URL: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
"""





def duplicate_count(text: str) -> int:
    """
    Esta función recibe una cadena de texto y devuelve el número de caracteres alfabéticos (en minúsculas) y dígitos numéricos 
    que aparecen más de una vez, sin distinguir entre mayúsculas y minúsculas.

    Args:
        text (str): La cadena de texto a analizar.

    Returns:
        int: El número de caracteres que aparecen más de una vez en la cadena, 
             sin distinguir entre mayúsculas y minúsculas.
    """
    char_count = {}

    # Convertimos el texto a minúsculas y contamos las ocurrencias de cada carácter
    for char in text.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    # Contamos cuántos caracteres tienen más de una ocurrencia
    count = 0
    for values in char_count.values():
        if values > 1:
            count += 1
    
    return count

def duplicate_count_alt(text: str) -> int:
    """
    Esta función recibe una cadena de texto y devuelve el número de caracteres alfabéticos (en minúsculas) y dígitos numéricos 
    que aparecen más de una vez, sin distinguir entre mayúsculas y minúsculas.
    Esta versión utiliza una lista por comprensión y la función `count()` para contar las ocurrencias.

    Args:
        text (str): La cadena de texto a analizar.

    Returns:
        int: El número de caracteres que aparecen más de una vez en la cadena, 
             sin distinguir entre mayúsculas y minúsculas.
    """
    # Convertimos toda la cadena a minúsculas para hacer la comparación insensible al caso.
    # Usamos set() para eliminar duplicados y asegurarnos de que cada carácter se cuente solo una vez.
    return len([char for char in set(text.lower()) if text.lower().count(char) > 1])

test1 = duplicate_count("aabBcde")
print(f"Resultado de la prueba 1: {test1}")  # Esperado: 2 (ya que 'a' y 'b' se repiten más de una vez)

test2 = duplicate_count("abcde")
print(f"Resultado de la prueba 2: {test2}")  # Esperado: 0 (ningún carácter se repite)

test3 = duplicate_count("aabBcdeff")
print(f"Resultado de la prueba 3: {test3}")  # Esperado: 2 (ya que 'a' y 'f' se repiten más de una vez)

test4 = duplicate_count("aabbcde")
print(f"Resultado de la prueba 4: {test4}")  # Esperado: 2 (ya que 'a' y 'b' se repiten más de una vez)

# Pruebas para la versión alternativa
test_alt1 = duplicate_count_alt("aabBcde")
print(f"Resultado de la prueba alternativa 1: {test_alt1}")  # Esperado: 2

test_alt2 = duplicate_count_alt("abcde")
print(f"Resultado de la prueba alternativa 2: {test_alt2}")  # Esperado: 0

test_alt3 = duplicate_count_alt("aabBcdeff")
print(f"Resultado de la prueba alternativa 3: {test_alt3}")  # Esperado: 2

test_alt4 = duplicate_count_alt("aabbcde")
print(f"Resultado de la prueba alternativa 4: {test_alt4}")  # Esperado: 2
