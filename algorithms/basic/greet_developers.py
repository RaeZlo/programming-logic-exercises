"""
You will be given an array of objects (associative arrays in PHP, tables in COBOL) representing data 
about developers who have signed up to attend the next coding meetup that you are organising.

Your task is to return an array where each object will have a new property 'greeting' with the following string value:
Hi < firstName here >, what do you like the most about < language here >?

URL: https://www.codewars.com/kata/58279e13c983ca4a2a00002a
"""





def greet_developers(persons: list[dict]) -> list[dict]:
    """
    Agrega un saludo personalizado a cada diccionario en la lista de desarrolladores.

    Args:
        persons (list[dict]): Lista de desarrolladores.

    Returns:
        list[dict]: La misma lista con una nueva clave 'greeting' en cada diccionario.
    """
    for person in persons:
        person['greeting'] = (
            f"Hi {person['firstName']}, what do you like the most about {person['language']}?"
        )
    return persons


list1 = [
    {
        'firstName': 'Sofia',
        'lastName': 'I.',
        'country': 'Argentina',
        'continent': 'Americas',
        'age': 35,
        'language': 'Java'
    },
    {
        'firstName': 'Lukas',
        'lastName': 'X.',
        'country': 'Croatia',
        'continent': 'Europe',
        'age': 35,
        'language': 'Python'
    }
]

result = greet_developers(list1)
for dev in result:
    print(dev['greeting'])
# Salida esperada:
# Hi Sofia, what do you like the most about Java?
# Hi Lukas, what do you like the most about Python?
