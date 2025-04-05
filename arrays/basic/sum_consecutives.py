"""
You are given a list/array which contains only integers (positive and negative). 
Your job is to sum only the numbers that are the same and consecutive. The result should be one list.

URL: https://www.codewars.com/kata/55eeddff3f64c954c2000059
"""





def sum_consecutives(numbers: list[int]) -> list[int]:
    """
    Agrupa números consecutivos iguales y suma cada grupo.

    Args:
        numbers (list[int]): Lista de enteros, positivos o negativos.

    Returns:
        list[int]: Lista con la suma de cada grupo consecutivo igual.
    """
    if not numbers:
        return []

    result = []
    current_sum = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_sum += numbers[i]
        else:
            result.append(current_sum)
            current_sum = numbers[i]
    
    result.append(current_sum)
    return result


print(sum_consecutives([1, 1, 2, 2, 2, 3]))        # [2, 6, 3]
print(sum_consecutives([1, -1, -1, 2]))            # [1, -2, 2]
print(sum_consecutives([3, 3, 3, 3, 3]))           # [15]
print(sum_consecutives([5]))                      # [5]
print(sum_consecutives([]))                       # []
print(sum_consecutives([1, 2, 3, 4]))              # [1, 2, 3, 4]
