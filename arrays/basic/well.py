"""
you need to check the provided array for good ideas 'good' and bad ideas 'bad'.
If there are one or two good ideas, return 'Publish!', if there are more than 2 
return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

URL: https://www.codewars.com/kata/57f222ce69e09c3630000212
"""





def well(ideas: list[str]) -> str:
    """
    Verifica cuántas ideas 'good' hay en la lista y devuelve un mensaje basado en ese conteo.

    Args:
        ideas (list[str]): Lista de ideas que puede contener las palabras 'good' y 'bad'.

    Returns:
        str: Mensaje basado en el número de ideas 'good'.
    """
    # Si hay al menos una idea 'good', revisamos cuántas hay
    if "good" in ideas:
        # Si hay más de dos ideas 'good', se devuelve 'I smell a series!'
        return "I smell a series!" if ideas.count("good") > 2 else "Publish!"
    else:
        # Si no hay ideas 'good', se devuelve 'Fail!'
        return "Fail!"
    
print(well(["bad", "good", "bad"]))  # Esperado: 'Publish!'
print(well(["good", "good", "bad", "bad"]))  # Esperado: 'Publish!'
print(well(["bad", "bad", "bad"]))  # Esperado: 'Fail!'
print(well(["good", "good", "good", "bad"]))  # Esperado: 'I smell a series!'
