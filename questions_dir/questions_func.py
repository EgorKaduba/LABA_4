import random

from questions_dir.questions import questions_dict as qd


def get_list_category() -> list:  # Получить список всех категорий
    return list(qd.keys())


def get_all_questions() -> list:  # Получить все вопросы
    res = []
    for val in qd.values():
        res = [*res, *val]
    return res


def get_random_question() -> dict:  # Получить рандомный вопрос
    return random.choice(get_all_questions())


def get_all_questions_category(category: str) -> list:  # Получить все вопросы из категории
    if category in get_list_category():
        for key, value in qd.items():
            if key == category:
                return value
    return list()


def get_random_question_category(category: str) -> dict:  # Получить рандомный вопрос из категории
    if category in get_list_category():
        return random.choice(qd[category])
    return dict()


def get_category_question(question: str) -> str:
    for key, value in qd.items():
        questions = [i['вопрос'] for i in value]
        if question in questions:
            return key
    return ""


def get_question_index(question: str) -> int:
    category = get_category_question(question)
    question_list = [i["вопрос"] for i in get_all_questions_category(category)]
    return question_list.index(question)
