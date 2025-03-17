"""
You need to write a function that calculates the total points our football team 
earned in a championship. Each match result is given as a string in the format "x:y", 
where x is our team's score and y is the opponent's score. The points are awarded as follows:

3 points for a win (x > y)
1 point for a tie (x = y)
0 points for a loss (x < y)

The function will receive a list of 10 match results and should return the total points our team earned.

URL: https://www.codewars.com/kata/5bb904724c47249b10000131
"""





def points(games:list[str]) -> int:
    """
    Calcula el total de puntos obtenidos en 10 partidos.

    Args:
        games (list[str]): Lista de cadenas con el formato "x:y", donde:
            - x es el puntaje de nuestro equipo.
            - y es el puntaje del equipo contrario.

    Returns:
        int: Total de puntos obtenidos según las reglas:
            - 3 puntos por victoria (x > y).
            - 1 punto por empate (x == y).
            - 0 puntos por derrota (x < y).
    """
    score = 0
    for i in games:
        score += 3 if i[0] > i[2] else 0
        score += 1 if i[0] == i[2] else 0
    return score

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))  # Esperado: 30 
print(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']))  # Esperado: 10 
print(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']))  # Esperado: 0 
print(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']))  # Esperado: 15 
print(points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']))  # Esperado: 12
