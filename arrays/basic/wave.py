"""
You need to create a function that turns a string into a "Mexican wave". You will be given a string, and you must return 
an array where each word has one letter in uppercase at a different position. The uppercase letter represents a person standing up.

Rules:
The input string will always be lowercase, but it may be empty.
If the character is a space, it should be ignored.

Example: For the string "hello", the result would be: ["Hello", "hEllo", "heLlo", "helLo", "hellO"].

URL: https://www.codewars.com/kata/58f5c63f1e26ecda7e000029
"""





def wave(people: str) -> list[str]:
    """
    Crea una lista con variaciones de la palabra, donde en cada índice una letra distinta está en mayúscula.

    Args:
        people (str): La cadena de entrada en minúsculas.

    Returns:
        list[str]: Lista con la "ola mexicana".
    """
    helper = []  # Lista para almacenar las variaciones de la palabra
    for i in range(len(people)):
        if people[i] == " ":  # Ignoramos los espacios
            continue
        else:
            # Convertimos la letra en la posición `i` a mayúscula
            new_str = people[:i] + people[i].upper() + people[i+1:]
            helper.append(new_str)  # Agregamos la nueva palabra a la lista
    return helper


def wave_alt(people: str) -> list[str]:
    """
    Versión alternativa con comprensión de listas.
    Genera la "ola mexicana" en una sola línea.

    Args:
        people (str): La cadena de entrada en minúsculas.

    Returns:
        list[str]: Lista con la "ola mexicana".
    """
    return [people[:i] + people[i].upper() + people[i+1:] for i in range(len(people)) if people[i].isalpha()]


print(wave("hello"))  # ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
print(wave_alt("hello"))  # ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
print(wave("gap"))  # ["Gap", "gAp", "gaP"]
print(wave_alt(" gap "))  # [" Gap ", " gAp ", " gaP "]
