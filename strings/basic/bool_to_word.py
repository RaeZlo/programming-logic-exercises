"""
Create a function that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

URL: https://www.codewars.com/kata/53369039d7ab3ac506000467
"""





def bool_to_word(boolean: bool) -> str:
    """
    Esta función recibe un valor booleano y devuelve una cadena de texto: 
    "Yes" si el valor es True, y "No" si el valor es False.
    
    Args:
        boolean (bool): Un valor booleano (True o False).
        
    Returns:
        str: "Yes" si el valor es True, "No" si el valor es False.
    """
    return "Yes" if boolean else "No"


test1 = bool_to_word(True)
print(test1)  # Esperado: "Yes"

test2 = bool_to_word(False)
print(test2)  # Esperado: "No"
