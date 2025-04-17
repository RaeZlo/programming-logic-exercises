"""
In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. 
Your task will be to return the sum of the numbers that occur only once.

For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. 
Every other number occurs twice.

More examples in the test cases.

URL: https://www.codewars.com/kata/59f11118a5e129e591000134
"""





def repeats(arr: list[int]) -> int:
    """
    Retorna la suma de los elementos que aparecen solo una vez en la lista.

    Args:
        arr (list[int]): Lista de enteros donde solo dos elementos aparecen una vez.

    Returns:
        int: Suma de los elementos únicos.
    """
    return sum(num for num in arr if arr.count(num) == 1)


print(repeats([4, 5, 7, 5, 4, 8]))       # 15 (7 + 8)
print(repeats([1, 2, 1, 3, 2, 4]))       # 7 (3 + 4)
print(repeats([10, 9, 10, 11, 12, 9]))   # 23 (11 + 12)
