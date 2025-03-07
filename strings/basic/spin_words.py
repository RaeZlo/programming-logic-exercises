"""
Write a function that takes in a string of one or more words, and returns the same string, 
but with all words that have five or more letters reversed. Strings passed in will consist of 
only letters and spaces. Spaces will be included only when more than one word is present.

URL: https://www.codewars.com/kata/5264d2b162488dc400000001
"""





def spin_words(sentence: str) -> str:
    """
    Esta función recibe una cadena de palabras y devuelve la misma cadena, 
    pero con las palabras que tienen cinco o más letras invertidas. Las cadenas 
    de entrada consisten solo en letras y espacios, y los espacios solo se incluyen 
    cuando hay más de una palabra.

    Args:
        sentence (str): La cadena de palabras a procesar.

    Returns:
        str: La cadena con las palabras de cinco o más letras invertidas.
    """
    return " ".join(word[::-1] if len(word) >= 5 else word for word in sentence.split())

# Pruebas de ejemplo
test1 = spin_words("Hey fellow warriors")
print(f"Resultado de la prueba 1: {test1}")  # Esperado: "Hey wollef sroirraw"

test2 = spin_words("This is a test")
print(f"Resultado de la prueba 2: {test2}")  # Esperado: "This is a test"
