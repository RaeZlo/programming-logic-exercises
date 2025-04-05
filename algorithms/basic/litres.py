"""
Nathan loves cycling.
Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.

URL: https://www.codewars.com/kata/582cb0224e56e068d800003c
"""





def litres(time: int) -> int:
    """
    Calcula la cantidad de litros que Nathan beberá durante su tiempo de ciclismo.

    Args:
        time (int): Cantidad de horas pedaleando.

    Returns:
        int: Litros de agua consumidos, redondeados hacia abajo.
    """
    return time // 2


print(litres(2))    # 1
print(litres(1.4))  # 0 (aunque solo se aceptan int, para decimal se redondearía hacia abajo)
print(litres(12))   # 6
print(litres(0))    # 0
print(litres(1787)) # 893
