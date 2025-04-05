"""
The task is to create a function called maskify that replaces all characters in a string (except for the last four) with the # symbol.

Rules:
If the string has more than four characters, replace all characters except the last four with #.
If the string has four or fewer characters, it remains unchanged.
If the string is empty, return an empty string.

URL: https://www.codewars.com/kata/5412509bd436bd33920011bc
"""





def maskify(cc: str) -> str:
    """
    Enmascara todos los caracteres de una cadena, excepto los últimos cuatro.

    Args:
        cc (str): Cadena de entrada.

    Returns:
        str: Cadena enmascarada con '#' excepto los últimos cuatro caracteres.
    """
    return f"{(len(cc) - 4) * '#'}{cc[-4:]}"


print(maskify("4556364607935616"))  # ############5616
print(maskify("1234"))              # 1234
print(maskify("abc"))               # abc
print(maskify(""))                  # ""
print(maskify("1"))                 # 1
