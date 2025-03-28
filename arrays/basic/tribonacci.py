"""
You need to create a function that generates the first n elements of a Tribonacci sequence. 
The sequence starts with 3 numbers (the signature), and each subsequent number is the sum of the previous 3 numbers.

Input:
A signature (array of 3 numbers).
n (number of elements to return).

Output:
Return the first n numbers of the Tribonacci sequence, including the signature.

If n == 0, return an empty array.

URL: https://www.codewars.com/kata/556deca17c58da83c00002db
"""





def tribonacci(signature:list[int], n:int) -> list[int]:
    """
    Genera los primeros n números de la secuencia Tribonacci.

    Args:
        signature (list[int]): Lista inicial de 3 números.
        n (int): Número total de elementos a generar.

    Returns:
        list[int]: Lista con los primeros n números de la secuencia Tribonacci.
    """
    helper = signature[:n]
    for _ in range(n - 3):
        helper.append(sum(helper[-3:]))
    return helper

print(tribonacci([1, 1, 1], 10))  # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
print(tribonacci([0, 0, 1], 10))  # [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
print(tribonacci([1, 2, 3], 0))   # []
print(tribonacci([1, 1, 1], 5))   # [1, 1, 1, 3, 5]
print(tribonacci([1, 2, 3], 3))   # [1, 2, 3]
