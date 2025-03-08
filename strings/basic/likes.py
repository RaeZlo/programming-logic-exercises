"""
The task requires implementing a function that generates a display message based on an array 
of people who like an item. The message should be tailored according to the number of people in the array:

- If no one likes the item, return "no one likes this".
- If only one person likes the item, return "<Name> likes this".
- If two people like it, return "<Name1> and <Name2> like this".
- If three people like it, return "<Name1>, <Name2>, and <Name3> like this".
- If more than three people like it, return "<Name1>, <Name2>, and <X> others like this", where X 
is the number of additional people beyond the first two.

The function should take an array of names as input and return the corresponding display message.

URL: https://www.codewars.com/kata/5266876b8f4bf2da9b000362
"""





def likes(names: list) -> str:
    """
    Esta función genera un mensaje personalizado basado en una lista de personas que gustan de un ítem.
    El mensaje varía según el número de personas en la lista:

    - Si nadie gusta del ítem, retorna "no one likes this".
    - Si solo una persona gusta del ítem, retorna "<Name> likes this".
    - Si dos personas gustan del ítem, retorna "<Name1> and <Name2> like this".
    - Si tres personas gustan del ítem, retorna "<Name1>, <Name2>, and <Name3> like this".
    - Si más de tres personas gustan del ítem, retorna "<Name1>, <Name2>, and <X> others like this", 
      donde X es el número de personas adicionales más allá de las dos primeras.

    Args:
        names (list): Lista de nombres de personas que gustan del ítem.

    Returns:
        str: El mensaje adecuado según la cantidad de personas en la lista.
    """
    if not names:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

# Pruebas de ejemplo
test1 = likes([]) 
print(f"Resultado de la prueba 1: {test1}")  # Esperado: "no one likes this"

test2 = likes(["Peter"]) 
print(f"Resultado de la prueba 2: {test2}")  # Esperado: "Peter likes this"

test3 = likes(["Jacob", "Alex"]) 
print(f"Resultado de la prueba 3: {test3}")  # Esperado: "Jacob and Alex like this"

test4 = likes(["Max", "John", "Mark"]) 
print(f"Resultado de la prueba 4: {test4}")  # Esperado: "Max, John and Mark like this"

test5 = likes(["Alex", "John", "Mark", "Jane", "Sara"]) 
print(f"Resultado de la prueba 5: {test5}")  # Esperado: "Alex, John and 3 others like this"
