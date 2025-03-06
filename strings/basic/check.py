"""
You will be given an array a and a value x. All you need to do is check whether the provided array
contains the value.
a can contain numbers or strings. x can be either.
Return true if the array contains the value, false if not.

URL: https://www.codewars.com/kata/57cc975ed542d3148f00015b
"""





def check(seq: list, elem) -> bool:
    """
    Esta función recibe una lista y un elemento, y verifica si el elemento está presente en la lista.
    
    Args:
        seq (list): La lista de elementos en la que se buscará el valor.
        elem: El valor que se busca dentro de la lista (puede ser un número o una cadena).
        
    Returns:
        bool: Devuelve True si el elemento está en la lista, False en caso contrario.
    """
    return elem in seq

test1 = check([1, 2, 3, 4, 5], 3)
print(f"¿Está el 3 en la lista? {test1}")  # Esperado: True

test2 = check(["manzana", "banana", "cereza"], "pera")
print(f"¿Está 'pera' en la lista? {test2}")  # Esperado: False
