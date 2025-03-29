"""
You have a string of words. You need to find the word with the highest score. 
Each letter has a score based on its position in the alphabet: a = 1, b = 2, c = 3, etc.

For example, the word "abad" has a score of 8 (1 + 2 + 1 + 4).
Return the word with the highest score. If two words have the same score, return the one that appears first in the original string.

URL: https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
"""





def high(words: str) -> str:
    """
    Encuentra la palabra con la puntuación más alta basada en la suma del valor de sus letras.

    Args:
        words (str): Cadena de palabras separadas por espacios.

    Returns:
        str: Palabra con la puntuación más alta.
    """
    words = words.split()  # Dividimos la cadena en una lista de palabras
    scores = []  # Lista para almacenar los puntajes de cada palabra
    for word in words:
        # Calculamos el puntaje de la palabra sumando el valor de cada letra
        # Se usa ord(char) - 96 porque 'a' en ASCII es 97, por lo que 'a' -> 1, 'b' -> 2, ..., 'z' -> 26
        score = sum(ord(char) - 96 for char in word)
        scores.append(score)  # Agregamos el puntaje a la lista
    # Buscamos la palabra con el puntaje más alto usando el índice del máximo en scores
    return words[scores.index(max(scores))]


# Versión alternativa optimizada
def high_alt(words: str) -> str:
    """
    Versión alternativa usando max() con una función clave para calcular la puntuación en una sola línea.
    """
    return max(words.split(), key=lambda word: sum(ord(char) - 96 for char in word))



print(high("hello world"))  # "world"
print(high("this is a test"))  # "this"
print(high("a b c d e f g"))  # "g"
print(high("aaa bbb ccc zzz"))  # "zzz"
print(high("abc xyz"))  # "xyz"
