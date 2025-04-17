"""
Implement a function, which takes a non-negative integer, representing the number of eggs to boil. 
It must return the time in minutes (integer), which it takes to have all the eggs boiled.

Rules
you can put at most 8 eggs into the pot at once
it takes 5 minutes to boil an egg
we assume, that the water is boiling all the time (no time to heat up)
for simplicity we also don't consider the time it takes to put eggs into the pot or get them out of it

URL: https://www.codewars.com/kata/52b5247074ea613a09000164
"""





def cooking_time(eggs: int) -> int:
    """
    Calcula el tiempo necesario para hervir todos los huevos en tandas de 8.

    Args:
        eggs (int): Número de huevos a hervir.

    Returns:
        int: Tiempo total en minutos.
    """
    batches = (eggs + 7) // 8  # Redondeo hacia arriba para saber cuántas tandas se necesitan
    return batches * 5


print(cooking_time(0))   # 0
print(cooking_time(5))   # 5
print(cooking_time(8))   # 5
print(cooking_time(10))  # 10
print(cooking_time(16))  # 10
print(cooking_time(25))  # 15
