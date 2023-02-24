import random

from question import Question
from data import questions_data


def load_questions():
    questions = []
    for question_data in questions_data:
        questions.append(Question(
            question_data["q"],
            question_data["d"],
            question_data["a"]
        ))
    random.shuffle(questions)
    return questions


def get_stats_from_questions(questions):
    correct_counter = 0
    points = 0

    for question in questions:
        if question.is_correct():
            correct_counter += 1
            points += question.get_points()

    print("Вот и всё!")
    print(f"Отвечено на {correct_counter} вопроса из {len(questions)}")
    print(f"Набрано баллов: {points}")