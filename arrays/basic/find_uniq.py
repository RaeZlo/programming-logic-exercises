"""
You are given an array of numbers. All numbers are the same except for one. Your task is to find that unique number.
It’s guaranteed that the array contains at least 3 numbers. Keep in mind that the tests may include large arrays, so focus on performance.

Examples:
Input: [1, 1, 1, 2, 1, 1]
Output: 2

URL: https://www.codewars.com/kata/585d7d5adb20cf33cb000235
"""





def find_uniq(arr: list[int]) -> int:
    """
    Encuentra el número único en la lista.

    Args:
        arr (list[int]): Lista de números enteros.

    Returns:
        int: El número que aparece una sola vez.
    """
    unique_numbers = set(arr)  # Convertimos la lista en un conjunto para obtener los valores únicos

    for num in unique_numbers:  # Iteramos sobre los números únicos
        if arr.count(num) == 1:  # Verificamos si aparece una sola vez en la lista original
            return num


print(find_uniq([1, 1, 1, 2, 1, 1]))  # 2
print(find_uniq([0, 0, 0.55, 0, 0]))  # 0.55
print(find_uniq([3, 3, 3, 3, 3, 3, 99]))  # 99
