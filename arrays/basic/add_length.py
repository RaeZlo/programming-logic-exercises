"""
Write a function that takes a string with words separated by spaces and returns a list where each word 
is followed by its length. The length should be added to the end of each word, separated by a space.

Example:
Input: "apple ban" → Output: ["apple 5", "ban 3"]

URL: https://www.codewars.com/kata/559d2284b5bb6799e9000047
"""





def add_length(sentence: str) -> list[str]:
    """
    Toma una cadena de palabras separadas por espacios y devuelve una lista 
    donde cada palabra está seguida por su longitud.

    Args:
        sentence (str): Cadena con palabras separadas por espacios.

    Returns:
        list[str]: Lista de palabras con sus longitudes adjuntas.
    """
    return [f"{word} {len(word)}" for word in sentence.split()]  # Genera la lista usando comprensión de listas

print(add_length("apple ban"))      # Esperado: ["apple 5", "ban 3"]
print(add_length("you will win"))   # Esperado: ["you 3", "will 4", "win 3"]
print(add_length("test case"))      # Esperado: ["test 4", "case 4"]
print(add_length("single"))         # Esperado: ["single 6"]
print(add_length(""))               # Esperado: [] (caso de cadena vacía)
