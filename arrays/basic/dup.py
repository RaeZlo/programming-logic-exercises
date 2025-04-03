"""
In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate 
letters from each string in the array.
Strings will be lowercase only, no spaces. See test cases for more examples.

URL: https://www.codewars.com/kata/59f08f89a5e129c543000069
"""





def dup(words: list[str]) -> list[str]:
    """
    Elimina letras duplicadas consecutivas en cada palabra de la lista.

    Args:
        words (list[str]): Lista de palabras.

    Returns:
        list[str]: Lista con palabras modificadas.
    """
    result = []
    for word in words:
        new_word = [word[0]]  # Iniciar con la primera letra
        for i in range(1, len(word)):
            if word[i] != word[i - 1]:  # Solo agregar si es diferente de la anterior
                new_word.append(word[i])
        result.append("".join(new_word))
    return result


print(dup(["hello", "bookkeeper"]))  # ["helo", "bokeper"]
print(dup(["aabbcc", "mississippi"]))  # ["abc", "misisipi"]
print(dup(["aaa", "bbb", "ccc"]))  # ["a", "b", "c"]
print(dup(["abcd", "effgghh"]))  # ["abcd", "efgh"]
print(dup([""]))  # [""]
