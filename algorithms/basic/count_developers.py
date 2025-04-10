"""
You will be given an array of objects (like Ruby hashes) containing information about developers who signed up for your coding meetup.
Your task is to count how many JavaScript developers come from Europe.

URL: https://www.codewars.com/kata/582746fa14b3892727000c4f
"""





def count_developers(persons: list[dict]) -> int:
    """
    Cuenta cuántos desarrolladores de JavaScript provienen de Europa.

    Args:
        persons (list[dict]): Lista de diccionarios con datos de cada persona.

    Returns:
        int: Número de desarrolladores que son de Europa y usan JavaScript.
    """
    return sum(
        1 for person in persons 
        if person.get("continent") == "Europe" and person.get("language") == "JavaScript"
    )


sample_data = [
    {"firstName": "Noah", "lastName": "M.", "country": "Switzerland", "continent": "Europe", "age": 19, "language": "JavaScript"},
    {"firstName": "Maia", "lastName": "S.", "country": "Tahiti", "continent": "Oceania", "age": 28, "language": "JavaScript"},
    {"firstName": "Shufen", "lastName": "L.", "country": "Taiwan", "continent": "Asia", "age": 35, "language": "HTML"},
    {"firstName": "Sumayah", "lastName": "M.", "country": "Tajikistan", "continent": "Asia", "age": 30, "language": "CSS"},
    {"firstName": "Maria", "lastName": "Y.", "country": "Spain", "continent": "Europe", "age": 30, "language": "JavaScript"},
]

print(count_developers(sample_data))  # 2
