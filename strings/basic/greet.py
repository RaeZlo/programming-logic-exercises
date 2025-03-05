"""
Create a function that accepts a parameter representing a name and returns the message: 
"Hello, <name> how are you doing today?".

URL: https://www.codewars.com/kata/55a70521798b14d4750000a4
"""





def greet(name: str) -> str:
    return f"Hello, {name} how are you doing today?"


test1 = greet("Pedro")
print(test1)  # Esperado: "Hello, Pedro how are you doing today?"

test2 = greet("Maria")
print(test2)  # Esperado: "Hello, Maria how are you doing today?"
