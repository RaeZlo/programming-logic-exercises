"""
Write a function that finds the largest sequence of 5 consecutive digits within a given number. 
The number will be passed as a string of digits. You should return the largest 5-digit sequence as an integer. 
The number can be as large as 1000 digits.

URL: https://www.codewars.com/kata/51675d17e0c1bed195000001
"""





def largest_consecutive_digits(digits: str) -> int:
    """
    Encuentra la mayor secuencia de 5 dígitos consecutivos en una cadena de números.

    Args:
        digits (str): Cadena de dígitos (hasta 1000 caracteres).

    Returns:
        int: El valor entero más alto de todas las subsecuencias de 5 dígitos.
    """
    numlist = [int(digits[i:i+5]) for i in range(0,len(digits)-4)]
    return max(numlist)


print(largest_consecutive_digits("1234567890"))  # 67890
print(largest_consecutive_digits("731674765"))   # 74765
print(largest_consecutive_digits("00000"))       # 0
