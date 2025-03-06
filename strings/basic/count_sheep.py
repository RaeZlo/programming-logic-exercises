"""
Given a non-negative integer, 3 for example, return a string with a murmur: 
"1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

URL: https://www.codewars.com/kata/5b077ebdaf15be5c7f00007
"""





def count_sheep(count: int) -> str:
    """
    Esta función recibe un número entero no negativo y genera una cadena que enumera las ovejas 
    siguiendo el formato: "1 sheep...2 sheep...3 sheep..." hasta el número proporcionado.
    
    Args:
        count (int): El número de ovejas a contar.
        
    Returns:
        str: La cadena generada con el formato adecuado.
    """
    return "".join(f"{i} sheep..." for i in range(1, count + 1))

# Ejemplo de prueba
test1 = count_sheep(3)
print(f"Cadena generada: {test1}")  # Esperado: "1 sheep...2 sheep...3 sheep..."

test2 = count_sheep(5)
print(f"Cadena generada: {test2}")  # Esperado: "1 sheep...2 sheep...3 sheep...4 sheep...5 sheep..."
