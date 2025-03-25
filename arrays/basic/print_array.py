"""
Given an array of elements, convert the elements into a string where each element is separated by a comma, 
maintaining the original order of the elements.

URL: https://www.codewars.com/kata/56e2f59fb2ed128081001328
"""





def print_array(elements: list) -> str:
    """
    Convierte una lista de elementos en un string separado por comas.

    Args:
        elements (list): Lista de elementos de cualquier tipo.

    Returns:
        str: String con los elementos separados por comas.
    """
    return ",".join(map(str, elements))  # Convierte cada elemento a string antes de unirlos


print(print_array([1, 2, 3]))  # Esperado: "1,2,3"
print(print_array(["a", "b", "c"]))  # Esperado: "a,b,c"
print(print_array([True, False, None]))  # Esperado: "True,False,None"
print(print_array([]))  # Esperado: "" (Lista vacía)
