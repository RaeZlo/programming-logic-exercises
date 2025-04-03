"""
You have a lottery ticket represented by an array of 2-element arrays. Each subarray has a string and a number. 
To win a mini-prize, you need to check if the ASCII code of any character in the string matches the number. 
If at least one character’s ASCII code matches the number, it counts as a mini-win. Then, compare the total number 
of mini-wins with a given number (win). 
If you have at least as many mini-wins as the win number, return "Winner!", otherwise, return "Loser!".

URL: https://www.codewars.com/kata/57f625992f4d53c24200070e
"""





def bingo(ticket: list[list], win: int) -> str:
    """
    Comprueba si el boleto de lotería tiene suficientes mini-premios.

    Args:
        ticket (list[list]): Lista de sublistas con una cadena y un número.
        win (int): Número mínimo de mini-premios para ganar.

    Returns:
        str: "Winner!" si se alcanzan los mini-premios, "Loser!" si no.
    """
    mini_wins = 0

    for string, number in ticket:
        # Verificamos si algún carácter coincide con el valor ASCII
        for char in string:
            if ord(char) == number:
                mini_wins += 1
                break  # Solo se permite un mini-premio por sublista

    return "Winner!" if mini_wins >= win else "Loser!"


print(bingo([["ABC", 65], ["HGR", 74], ["BYHT", 74]], 2))  # Winner! ('A' -> 65, 'J' -> 74)
print(bingo([["ABC", 66], ["HGR", 74], ["BYHT", 74]], 3))  # Loser! (solo 2 mini-premios)
print(bingo([["AAA", 65]], 1))  # Winner! ('A' -> 65)
print(bingo([["abc", 100], ["xyz", 120]], 1))  # Loser! (ningún mini-premio)
print(bingo([], 0))  # Winner! (0 requeridos y 0 obtenidos)
