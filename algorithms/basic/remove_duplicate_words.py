"""
Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

URL: https://www.codewars.com/kata/5b39e3772ae7545f650000fc
"""





def remove_duplicate_words(words: str) -> str:
    """
    Elimina palabras duplicadas manteniendo el orden y la primera aparición.

    Args:
        words (str): Frase con posibles palabras repetidas.

    Returns:
        str: Frase sin duplicados, manteniendo el orden original.
    """
    helper = []
    for word in words.split():
        if word not in helper:
            helper.append(word)
    return " ".join(helper)


def remove_duplicate_words_alt(words: str) -> str:
    """
    Versión compacta usando set y sorted para eliminar duplicados.

    Args:
        words (str): Frase con posibles palabras repetidas.

    Returns:
        str: Frase sin duplicados, manteniendo el orden original.
    """
    return ' '.join(sorted(set(words.split()), key=words.index))


print(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))  # "alpha beta gamma delta"
