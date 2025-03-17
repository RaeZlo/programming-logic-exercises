"""
Write a function that takes an array of strings as an argument and returns a sorted array containing 
the same strings, ordered from shortest to longest.
All of the strings in the array passed to your function will be different lengths, so you will not have 
to decide how to order multiple strings of the same length.

URL: https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c
"""





def sort_by_length(arr: list[str]) -> list[str]:
    """
    Ordena una lista de strings según su longitud.

    Args:
        arr (list[str]): Lista de strings.

    Returns:
        list[str]: Lista ordenada de menor a mayor longitud.
    """
    return sorted(arr, key=len)


print(sort_by_length(["apple", "pie", "banana", "a"]))  # Esperado: ['a', 'pie', 'apple', 'banana']
print(sort_by_length(["dog", "cat", "elephant", "bat"]))  # Esperado: ['dog', 'cat', 'bat', 'elephant']
print(sort_by_length(["abc", "a", "abcd", "ab"]))  # Esperado: ['a', 'ab', 'abc', 'abcd']
print(sort_by_length(["python", "c", "java", "golang"]))  # Esperado: ['c', 'java', 'python', 'golang']
