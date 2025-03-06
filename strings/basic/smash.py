"""
Write a function that takes an array of words and smashes them together into a sentence 
and returns the sentence. You can ignore any need to sanitize words or add punctuation, 
but you should add spaces between each word. Be careful, there shouldn't be a space at the 
beginning or the end of the sentence!

URL: https://www.codewars.com/kata/53dc23c68a0c93699800041d
"""





def smash(words: list) -> str:
    """
    Esta función recibe una lista de palabras y las combina en una sola cadena de texto, 
    separadas por espacios. No debe haber un espacio al principio ni al final de la cadena.
    
    Args:
        words (list): La lista de palabras que se desean combinar.
        
    Returns:
        str: La cadena de texto resultante, con las palabras separadas por espacios.
    """
    return " ".join(words)

# Ejemplo de prueba
test1 = smash(["Hola", "mundo", "esto", "es", "genial"])
print(f"Frase resultante: {test1}")  # Esperado: "Hola mundo esto es genial"

test2 = smash(["Python", "es", "genial"])
print(f"Frase resultante: {test2}")  # Esperado: "Python es genial"
