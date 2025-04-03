"""
Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, 
while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are a 
part of the word in this kata.

URL: https://www.codewars.com/kata/58d76854024c72c3e20000de
"""





def reverse_alternate(text: str) -> str:
    """
    Invierte cada segunda palabra en una cadena.

    Args:
        text (str): Texto de entrada.

    Returns:
        str: Texto con las palabras alternas invertidas.
    """
    words = text.split()
    for i in range(1, len(words), 2):  # Iterar solo sobre palabras en posiciones impares
        words[i] = words[i][::-1]  # Invertir palabra
    return " ".join(words)


def reverse_alternate_alt(text: str) -> str:
    """
    Variante con comprensión de listas.
    """
    return " ".join(word[::-1] if i % 2 else word for i, word in enumerate(text.split()))



print(reverse_alternate("Hello world!"))         # "Hello !dlrow"
print(reverse_alternate("This is a test"))       # "This si a tset"
print(reverse_alternate("Another  example  here"))  # "Another elpmaxe here"
print(reverse_alternate("   Keep   spaces   "))  # "Keep secaps"
print(reverse_alternate(""))                     # "" (cadena vacía)
