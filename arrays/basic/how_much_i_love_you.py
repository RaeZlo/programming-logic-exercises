"""
You are given a flower with a certain number of petals. Starting with the phrase "I love you," 
each petal is torn while repeating a specific sequence of phrases:

1. "I love you"
2. "a little"
3. "a lot"
4. "passionately"
5. "madly"
6. "not at all"

If the number of petals exceeds 6, the sequence repeats. Your task is to determine which phrase 
corresponds to the last petal. The number of petals is always greater than 0.

URL: https://www.codewars.com/kata/57f24e6a18e9fad8eb000296
"""





def how_much_i_love_you(petals: int) -> str:
    """
    Determina la frase correspondiente al último pétalo arrancado.

    Args:
        petals (int): Número de pétalos de la flor.

    Returns:
        str: Frase correspondiente al último pétalo según el patrón cíclico.
    """
    # Lista de frases que se repiten en orden cíclico cada 6 pétalos
    phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    
    # Se usa el módulo (%) para obtener el índice correcto dentro del ciclo de 6 frases
    return phrases[(petals - 1) % 6]

print(how_much_i_love_you(1))  # Esperado: "I love you"
print(how_much_i_love_you(2))  # Esperado: "a little"
print(how_much_i_love_you(6))  # Esperado: "not at all"
print(how_much_i_love_you(7))  # Esperado: "I love you" (se reinicia el ciclo)
print(how_much_i_love_you(10)) # Esperado: "passionately"
print(how_much_i_love_you(15)) # Esperado: "madly"
print(how_much_i_love_you(20)) # Esperado: "a lot"
