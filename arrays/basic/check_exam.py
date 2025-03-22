"""
Given two arrays:
- The first array represents the correct answers to an exam.
- The second array contains a student's submitted answers.

Scoring rules:
- +4 for each correct answer.
- -1 for each incorrect answer.
- 0 for each blank answer (empty string or space).

If the total score is less than 0, return 0.

URL: https://www.codewars.com/kata/5a3dd29055519e23ec000074
"""





def check_exam(correct_answers: list[str], student_answers: list[str]) -> int:
    """
    Calcula la puntuación de un examen comparando las respuestas correctas con las del estudiante.

    Args:
        correct_answers (list[str]): Lista con las respuestas correctas.
        student_answers (list[str]): Lista con las respuestas del estudiante.

    Returns:
        int: Puntuación final basada en las reglas de evaluación.
    """
    score = 0  # Inicializamos la puntuación en 0

    # Iteramos sobre ambas listas al mismo tiempo con zip()
    for correct, student in zip(correct_answers, student_answers):
        if student == correct:  
            score += 4  # Suma 4 puntos por cada respuesta correcta
        elif student.strip() == "":  
            score += 0  # No suma ni resta puntos si la respuesta está vacía o es un espacio
        else:  
            score -= 1  # Resta 1 punto por cada respuesta incorrecta

    return max(score, 0)  # Si el puntaje es negativo, devuelve 0

print(check_exam(["a", "b", "c", "d"], ["a", "b", "c", "d"]))  # Esperado: 16 (todas correctas)
print(check_exam(["a", "b", "c", "d"], ["a", "b", "x", ""]))  # Esperado: 7 (2 correctas, 1 incorrecta, 1 vacía)
print(check_exam(["a", "b", "c", "d"], ["x", "x", "x", "x"]))  # Esperado: 0 (todas incorrectas, pero no puede ser negativo)
print(check_exam(["a", "b", "c", "d"], ["", " ", "c", "d"]))  # Esperado: 8 (2 vacías, 2 correctas)
