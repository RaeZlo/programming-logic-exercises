"""
You will be given an array of objects (associative arrays in PHP) representing data about developers who have 
signed up to attend the next coding meetup that you are organising.

Your task is to return:
true if at least one Ruby developer has signed up; or
false if there will be no Ruby developers.
For example, given the following input array:

list1 = [
    { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java' },
    { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python' },
    { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby' } 
    ]

URL: https://www.codewars.com/kata/5827acd5f524dd029d0005a4
"""





def is_ruby_coming(persons: list[dict]) -> bool:
    """
    Verifica si al menos un desarrollador usa Ruby como lenguaje.

    Args:
        persons (list[dict]): Lista de diccionarios con datos de desarrolladores.

    Returns:
        bool: True si hay al menos un desarrollador Ruby, False en caso contrario.
    """
    return any(person.get('language') == 'Ruby' for person in persons)


list1 = [
    { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java' },
    { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python' },
    { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby' }
]

list2 = [
    { 'firstName': 'Carlos', 'lastName': 'Z.', 'country': 'Spain', 'continent': 'Europe', 'age': 29, 'language': 'JavaScript' }
]

print(is_ruby_coming(list1))  # True
print(is_ruby_coming(list2))  # False
