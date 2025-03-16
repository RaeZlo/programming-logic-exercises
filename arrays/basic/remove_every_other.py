"""
Take an array and remove every second element from the array. Always keep the first 
element and start removing with the next element.

URL: https://www.codewars.com/kata/5769b3802ae6f8e4890009d2
"""





def remove_every_other(my_list: list) -> list:
    """
    Esta función recibe una lista y retorna una nueva lista con cada segundo elemento eliminado.
    Se mantiene el primer elemento y se eliminan los siguientes en posiciones impares.

    Args:
        my_list (list): Lista de elementos de cualquier tipo.

    Returns:
        list: Lista sin los elementos en posiciones impares.
    """
    return [value for key, value in enumerate(my_list) if key % 2 == 0]  

def remove_every_other_alt(my_list: list) -> list:
    """
    Alternativa utilizando el slicing para obtener solo los elementos en posiciones pares.

    Args:
        my_list (list): Lista de elementos de cualquier tipo.

    Returns:
        list: Lista sin los elementos en posiciones impares.
    """
    return my_list[::2] 


print(remove_every_other(["a", "b", "c", "d", "e"]))  # Esperado: ['a', 'c', 'e']
print(remove_every_other_alt([1, 2, 3, 4, 5, 6]))        # Esperado: [1, 3, 5]
print(remove_every_other(["Hola", "Mundo"]))         # Esperado: ['Hola']
print(remove_every_other([42]))                      # Esperado: [42] (caso borde con un solo elemento)
print(remove_every_other([]))                        # Esperado: [] (caso borde con lista vacía)
