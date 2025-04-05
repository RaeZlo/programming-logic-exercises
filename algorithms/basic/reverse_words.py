"""
Complete the solution so that it reverses all of the words within the string passed in.
Words are separated by exactly one space and there are no leading or trailing spaces.

URL: https://www.codewars.com/kata/51c8991dee245d7ddf00000e
"""





def reverse_words(text: str) -> str:
    """
    Invierte el orden de las palabras en una cadena.

    Args:
        text (str): Cadena de entrada con palabras separadas por un espacio.

    Returns:
        str: Cadena con el orden de palabras invertido.
    """
    return " ".join(text.split()[::-1])


print(reverse_words("The quick brown fox"))    # "fox brown quick The"
print(reverse_words("Hello world!"))           # "world! Hello"
print(reverse_words("Codewars"))               # "Codewars"
print(reverse_words("Python is fun"))          # "fun is Python"
