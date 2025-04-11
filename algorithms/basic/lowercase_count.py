"""
Your task is simply to count the total number of lowercase letters in a string.

URL: https://www.codewars.com/kata/56a946cd7bd95ccab2000055
"""





def lowercase_count(text: str) -> int:
    """
    Cuenta la cantidad de letras minúsculas en un string.

    Args:
        text (str): Cadena de texto a evaluar.

    Returns:
        int: Número total de letras minúsculas.
    """
    return sum(char.islower() for char in text)


print(lowercase_count("abcABC123"))     # 3
print(lowercase_count("ABC"))           # 0
print(lowercase_count("a1b2c3"))        # 3
print(lowercase_count(""))              # 0
