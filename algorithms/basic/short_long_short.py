"""
Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer 
string on the inside. The strings will not be the same length, but they may be empty ( zero length ).

URL: https://www.codewars.com/kata/50654ddff44f800200000007
"""





def short_long_short(a: str, b: str) -> str:
    """
    Retorna una nueva cadena con el formato corto+largo+corto según la longitud de las cadenas dadas.

    Args:
        a (str): Primera cadena.
        b (str): Segunda cadena.

    Returns:
        str: Cadena formada por la concatenación corto+largo+corto.
    """
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a


print(short_long_short("1", "22"))        # "1221"
print(short_long_short("hello", "hi"))    # "hihellohi"
print(short_long_short("", "abc"))        # "abc"
print(short_long_short("a", ""))          # "a"
