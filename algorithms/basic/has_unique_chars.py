"""
Write a program to determine if a string contains only unique characters. Return true if it does and false otherwise.

The string may contain any of the 128 ASCII characters. Characters are case-sensitive, e.g. 'a' and 'A' are considered 
different characters.

URL: https://www.codewars.com/kata/553e8b195b853c6db4000048/train/python
"""





def has_unique_chars(string: str) -> bool:
    """
    Verifica si una cadena contiene solo caracteres únicos.

    Args:
        string (str): Cadena de entrada.

    Returns:
        bool: True si todos los caracteres son únicos, False si hay repetidos.
    """
    return len(string) == len(set(string))


print(has_unique_chars("abcdef"))     # True
print(has_unique_chars("AaBbCc"))     # True
print(has_unique_chars("hello"))      # False
print(has_unique_chars(""))           # True
print(has_unique_chars("1234567890")) # True
