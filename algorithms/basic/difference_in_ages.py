"""
At the family reunion, we want to find the age difference between the youngest and the oldest family member. 
You will be given a list of ages of all the family members. The ages are whole numbers, so for example, a 5-month-old baby 
will have an age of 0. You need to return a list (or tuple) with these three numbers:

The youngest age.
The oldest age.
The difference between the youngest and the oldest age.

URL: https://www.codewars.com/kata/5720a1cb65a504fdff0003e2
"""





def difference_in_ages(ages: list[int]) -> tuple:
    """
    Calcula la edad más joven, la más vieja y su diferencia.

    Args:
        ages (list[int]): Lista de edades enteras.

    Returns:
        tuple: (edad_menor, edad_mayor, diferencia)
    """
    return (min(ages), max(ages), max(ages) - min(ages))


print(difference_in_ages([82, 15, 6, 38, 35]))  # (6, 82, 76)
print(difference_in_ages([0, 0, 0]))            # (0, 0, 0)
print(difference_in_ages([5, 99]))              # (5, 99, 94)
