"""
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

URL: https://www.codewars.com/kata/57356c55867b9b7a60000bd7
"""






def basic_op(operator: str, value1: int, value2: int) -> int:
    """
    Esta función recibe tres argumentos: un operador en forma de cadena (string o carácter), 
    y dos números enteros. La función realiza la operación correspondiente entre los dos números 
    y devuelve el resultado.
    
    Args:
        operator (str): El operador que indica la operación a realizar ('+', '-', '*', '/').
        value1 (int): El primer número para la operación.
        value2 (int): El segundo número para la operación.
        
    Returns:
        int: El resultado de aplicar la operación entre value1 y value2.
        None: Si se intenta dividir por cero.
    """
    match operator:
        case "+":
            return value1 + value2
        case "-":
            return value1 - value2
        case "*":
            return value1 * value2
        case "/":
            return value1 / value2
        

# Ejemplos de prueba
test1 = basic_op("/", 2, 5)
print(f"El resultado de la operacion da: {test1}")  # Esperado: 0.4

test2 = basic_op("*", 2, 5)
print(f"El resultado de la operacion da: {test2}")  # Esperado: 10
