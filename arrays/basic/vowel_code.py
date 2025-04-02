"""
encode() function: Create a function that replaces all lowercase vowels in a string with numbers based on this pattern:
a -> 1, e -> 2, i -> 3, o -> 4, u -> 5

Example: encode("hello") should return "h2ll4".

decode() function: Create another function that turns the numbers back into their corresponding vowels.
Example: decode("h3 th2r2") should return "hi there".

URL: https://www.codewars.com/kata/53697be005f803751e0015aa
"""





def encode(text: str) -> str:
    """
    Reemplaza las vocales por números según la conversión dada.

    Args:
        text (str): Texto a codificar.

    Returns:
        str: Texto con las vocales reemplazadas por números.
    """
    for num, char in enumerate("aeiou", start=1):
        text = text.replace(char, str(num))
    return text


def decode(text: str) -> str:
    """
    Reemplaza los números por las vocales originales.

    Args:
        text (str): Texto codificado.

    Returns:
        str: Texto decodificado con las vocales originales.
    """
    for num, char in enumerate("aeiou", start=1):
        text = text.replace(str(num), char)
    return text



print(encode("hello"))      # "h2ll4"
print(encode("programming"))  # "pr4gr1mm3ng"
print(encode("a quick fox"))  # "1 q53ck f4x"

print(decode("h2ll4"))      # "hello"
print(decode("pr4gr1mm3ng"))  # "programming"
print(decode("1 q53ck f4x"))  # "a quick fox"
