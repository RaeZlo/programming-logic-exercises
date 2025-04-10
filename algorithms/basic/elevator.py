"""
You have two elevators, named "left" and "right", in a building with 3 floors (numbered 0 to 2).

Your task is to write a function that takes three arguments:
left: the current floor of the left elevator
right: the current floor of the right elevator
call: the floor that called the elevator

The function should return the name of the closest elevator ("left" or "right").
If both elevators are equally distant from the called floor, choose the right elevator.

URL: https://www.codewars.com/kata/5c374b346a5d0f77af500a5a
"""





def elevator(left: int, right: int, call: int) -> str:
    """
    Determina cuál ascensor está más cerca del piso solicitado.

    Args:
        left (int): Piso actual del ascensor izquierdo.
        right (int): Piso actual del ascensor derecho.
        call (int): Piso desde donde se llamó al ascensor.

    Returns:
        str: "left" si el izquierdo está más cerca, "right" si el derecho está más cerca o igual de cerca.
    """
    return "left" if abs(call - left) < abs(call - right) else "right"


print(elevator(0, 2, 1))  # "right", ambos a distancia 1, elige el derecho
print(elevator(0, 1, 0))  # "left", el izquierdo ya está en el piso
print(elevator(2, 1, 0))  # "right", distancia 2 vs 1
