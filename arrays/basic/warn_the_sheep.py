"""
You are standing at the front of a queue of animals, with the wolf somewhere in the array. 
If the wolf is immediately in front of you (the closest to the front), return the message 'Pls go away and stop eating my sheep'. 
Otherwise, warn the sheep that is closest to the wolf by returning 'Oi! Sheep number N! You are about to be eaten by a wolf!' 
where N is the position of the sheep closest to the wolf.

URL: https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15
"""





def warn_the_sheep(queue: list[str]) -> str:
    """
    Identifica la posición del lobo en la fila y advierte al animal en riesgo.

    Args:
        queue (list[str]): Lista de animales en la fila, donde 'wolf' representa al lobo.

    Returns:
        str: Mensaje de advertencia adecuado según la posición del lobo.
    """
    wolf_index = queue.index("wolf")  # Encuentra la posición del lobo en la lista
    
    if queue[-1] == "wolf":  # Si el lobo está al final de la fila (más cercano al usuario)
        return "Pls go away and stop eating my sheep"
    
    # Calculamos el número del oveja en riesgo (desde la perspectiva del usuario al final)
    sheep_number = len(queue) - wolf_index - 1
    return f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!"

print(warn_the_sheep(["sheep", "sheep", "wolf", "sheep"]))  # Esperado: "Oi! Sheep number 1! You are about to be eaten by a wolf!
print(warn_the_sheep(["sheep", "sheep", "sheep", "wolf"]))  # Esperado: "Pls go away and stop eating my sheep"
print(warn_the_sheep(["wolf", "sheep", "sheep", "sheep"]))  # Esperado: "Oi! Sheep number 3! You are about to be eaten by a wolf!"
