"""
You are given a string containing a sequence of character sequences separated by commas. 
Write a function that returns a new string containing the same character sequences except 
for the first and last ones, but this time separated by spaces. If the input string is empty 
or if removing the first and last items results in an empty string, return an empty value 
(represented as NULL in the examples below).

URL: https://www.codewars.com/kata/570597e258b58f6edc00230d
"""





def array(string: str) -> str | None:
    """
    Procesa el string eliminando la primera y última secuencia.

    Args:
        string (str): Cadena de texto separada por comas.

    Returns:
        str | None: Nueva cadena con los elementos intermedios separados por espacios,
                    o None si no hay elementos suficientes.
    """
    parts = string.split(",")  # Dividir la cadena en una lista
    if len(parts) < 3:  # Si hay menos de 3 elementos, no hay intermedios
        return None
    
    return " ".join(parts[1:-1])  # Unir los elementos intermedios con espacios


print(array("1,2,3"))  # Esperado: "2"
print(array("a,b,c,d"))  # Esperado: "b c"
print(array("apple,banana,grape,orange"))  # Esperado: "banana grape"
print(array("hello"))  # Esperado: None (Solo un elemento)
print(array(""))  # Esperado: None (Cadena vacía)
print(array("1,2"))  # Esperado: None (No hay elementos intermedios)
