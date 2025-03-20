"""
You are at the zoo, and the meerkats have their heads and tails switched! 
Your task is to fix them by rearranging an array with three values: tail, body, and head. 
You need to reorder the array so that it becomes head, body, and tail. 
Do the same for all other arrays you receive in the tests.

URL: https://www.codewars.com/kata/56f699cd9400f5b7d8000b55
"""





def fix_the_meerkat(arr: list[str]) -> list[str]:
    """
    Reordena la lista para que siga el orden correcto: cabeza, cuerpo y cola.

    Args:
        arr (list[str]): Lista de tres elementos en orden incorrecto (cola, cuerpo, cabeza).

    Returns:
        list[str]: Lista reordenada en el orden correcto (cabeza, cuerpo, cola).
    """
    return arr[::-1]  # Invierte el orden de los elementos de la lista

print(fix_the_meerkat(["tail", "body", "head"]))  # Esperado: ["head", "body", "tail"]
print(fix_the_meerkat(["lower legs", "torso", "upper body"]))  # Esperado: ["upper body", "torso", "lower legs"]
print(fix_the_meerkat(["feet", "belly", "face"]))  # Esperado: ["face", "belly", "feet"]
