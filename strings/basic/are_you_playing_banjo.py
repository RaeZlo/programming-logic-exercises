'''
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"

URL: https://www.codewars.com/kata/53af2b8861023f1d88000832
'''





def are_you_playing_banjo(name: str) -> str:
    """
    Esta función recibe un nombre y determina si la persona está tocando el banjo 
    en función de la primera letra del nombre. Si el nombre comienza con "R" o "r", 
    se asume que está tocando el banjo, y devuelve el mensaje correspondiente.

    Args:
        name (str): El nombre de la persona.

    Returns:
        str: Un mensaje indicando si la persona toca el banjo o no.
    """
    if name[0].lower() == 'r':
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'


test1 = are_you_playing_banjo("Rafael")
print(test1)  # Esperado: "Rafael plays banjo"

test2 = are_you_playing_banjo("Carlos")
print(test2)  # Esperado: "Carlos does not play banjo"
