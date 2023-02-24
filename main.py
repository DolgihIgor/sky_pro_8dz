from utils import load_questions, get_stats_from_questions


def main():

    questions = load_questions()

    for question in questions:

        print(question.build_question())
        user_answer = input()
        question.user_answer = user_answer

        if question.is_correct():
            print(question.build_positive_feedback())
        else:
            print(question.build_negative_feedback())

    get_stats_from_questions(questions)


main()
