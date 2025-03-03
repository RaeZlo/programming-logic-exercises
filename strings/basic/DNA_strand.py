"""
The task is to convert a given DNA string into its complementary strand. In the DNA sequence, 
the complementary bases are:

"A" pairs with "T"
"T" pairs with "A"
"C" pairs with "G"
"G" pairs with "C"
Given a DNA string, you need to return the complementary strand where each base is replaced by its complement.

URL: https://www.codewars.com/kata/554e4a2f232cdd87d9000038
"""





def DNA_strand(dna: str) -> str:
    """
    Esta función recibe una cadena de ADN y devuelve su hebra complementaria, 
    reemplazando cada base por su complementaria según las reglas estándar:
    - "A" se convierte en "T"
    - "T" se convierte en "A"
    - "C" se convierte en "G"
    - "G" se convierte en "C"
    
    Args:
        dna (str): La cadena de ADN a convertir.
        
    Returns:
        str: La cadena de ADN complementaria.
    """
    replace = {"A": "T", 
               "T": "A", 
               "C": "G", 
               "G": "C"}
    return "".join(replace[char] for char in dna)

# Pruebas de ejemplo
test1 = DNA_strand("ATTGC")
print(f"Resultado de la prueba 1: {test1}")  # Esperado: "TAACG"

test2 = DNA_strand("GTAT")
print(f"Resultado de la prueba 2: {test2}")  # Esperado: "CATA"
