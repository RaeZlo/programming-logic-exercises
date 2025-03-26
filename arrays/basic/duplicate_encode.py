"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" 
if that character appears only once in the original string, or ")" if that character appears more than once in 
the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"

URL: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
"""





def duplicate_encode(word: str) -> str:
    """
    Convierte una palabra en una cadena con "(" o ")" dependiendo de la cantidad de ocurrencias de cada letra.

    Args:
        word (str): La palabra de entrada.

    Returns:
        str: La nueva cadena con "(" para caracteres únicos y ")" para caracteres repetidos.
    """
    # Convierte la palabra a minúsculas para ignorar la capitalización.
    word = word.lower()
    # Genera una lista con "(" para caracteres únicos y ")" para caracteres repetidos.
    encoded = [")" if word.count(char) > 1 else "(" for char in word]
    # Une la lista en una cadena y la devuelve.
    return "".join(encoded)


print(duplicate_encode("din"))      # "((("
print(duplicate_encode("recede"))   # "()()()"
print(duplicate_encode("Success"))  # ")())())" (ignora mayúsculas/minúsculas)
print(duplicate_encode("(( @"))     # "))(("
