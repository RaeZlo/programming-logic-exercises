"""
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to 
the smallest value.

URL: https://www.codewars.com/kata/582cb0224e56e068d800003c
"""





def litres(time:int) -> int:
    """
    Esta función calcula la cantidad de agua que Nathan debe beber en función del tiempo de ciclismo,
    redondeada hacia el valor entero más pequeño.
    
    Args:
        time (int): El tiempo de ciclismo en horas.
        
    Returns:
        int: La cantidad de litros de agua que Nathan debe beber, redondeada hacia el valor más pequeño.
    """
    return time // 2

test1 = litres(3)
print(f"Los litros de agua a tomar son: {test1}")

test2 = litres(11)
print(f"Los litros de agua a tomar son: {test2}")
