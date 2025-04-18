"""
Number is a palindrome if it is equal to the number with digits in reversed order. For example, 5, 44, 171, 4884 are palindromes, 
and 43, 194, 4773 are not.

Write a function which takes a positive integer and returns the number of special steps needed to obtain a palindrome. 
The special step is: "reverse the digits, and add to the original number". If the resulting number is not a palindrome, 
repeat the procedure with the sum until the resulting number is a palindrome.

If the input number is already a palindrome, the number of steps is 0.


URL: https://www.codewars.com/kata/525f039017c7cd0e1a000a26
"""





def palindrome_chain_length(n: int) -> int:
    """
    Calcula el número de pasos necesarios para convertir un número en un palíndromo,
    sumándolo con su reverso en cada paso.

    Args:
        n (int): Número positivo inicial.

    Returns:
        int: Número de pasos necesarios para obtener un palíndromo.
    """
    count = 0
    while str(n) != str(n)[::-1]:
        n += int(str(n)[::-1])
        count += 1
    return count


print(palindrome_chain_length(87))     # 4 (87+78=165, 165+561=726, 726+627=1353, 1353+3531=4884)
print(palindrome_chain_length(44))     # 0 (ya es palíndromo)
print(palindrome_chain_length(10))     # 1 (10+01=11)
