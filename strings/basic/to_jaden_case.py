"""
Convert the given string to "Jaden Case", where each word is capitalized. 
Keep contractions in their original form (e.g., "aren't" should stay as "Aren't").

Example:
Input: "How can mirrors be real if our eyes aren't real"
Output: "How Can Mirrors Be Real If Our Eyes Aren't Real"

URL: https://www.codewars.com/kata/5390bac347d09b7da40006f6
"""





def to_jaden_case(text:str) -> str:
    """
    Esta función recibe una cadena de texto y convierte cada palabra a "Jaden Case", 
    donde cada palabra empieza con mayúscula.

    Args:
        text (str): La cadena de texto a convertir.

    Returns:
        str: La cadena de texto con cada palabra en Jaden Case, manteniendo las contracciones tal como están.
    """
    return " ".join(word.capitalize() for word in text.split())

test1 = to_jaden_case("How can mirrors be real if our eyes aren't real")
print(f"Resultado de la prueba 1: {test1}")  # Esperado: "How Can Mirrors Be Real If Our Eyes Aren't Real"

test2 = to_jaden_case("I can't believe it's not butter!")
print(f"Resultado de la prueba 2: {test2}")  # Esperado: "I Can't Believe It's Not Butter!"
