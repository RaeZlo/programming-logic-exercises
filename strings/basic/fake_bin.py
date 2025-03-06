"""
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and 
above with '1'. Return the resulting string.
Note: input will never be an empty string

URL: https://www.codewars.com/kata/57eae65a4321032ce000002d
"""





def fake_bin(digits: str) -> str:
    """
    Esta función recibe una cadena de dígitos y reemplaza cualquier dígito menor que 5 con '0'
    y cualquier dígito mayor o igual a 5 con '1'. Devuelve la cadena resultante.
    
    Args:
        digits (str): La cadena de dígitos que se desea transformar.
        
    Returns:
        str: La cadena resultante con '0' para dígitos menores a 5 y '1' para los dígitos mayores o iguales a 5.
    """
    return "".join("1" if int(digit) >= 5 else "0" for digit in digits)

# Ejemplo de prueba
test1 = fake_bin("3456789")
print(f"Cadena resultante: {test1}")  # Esperado: "0011111"

test2 = fake_bin("1234567890")
print(f"Cadena resultante: {test2}")  # Esperado: "0001111000"
