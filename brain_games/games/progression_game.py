from random import randint


LOWER_LIMIT = 1
START_UPPER_LIMIT = 20
STEP_UPPER_LIMIT = 10
LENGTH = 10
DESCRIPTION = 'What number is missing in the progression?'


def get_round_data():
    list = []
    start = randint(LOWER_LIMIT, START_UPPER_LIMIT)
    step = randint(LOWER_LIMIT, STEP_UPPER_LIMIT)
    end = start + (LENGTH * step)

    for index in range(start, end, step):
        list.append(str(index))

    limit = len(list) - 1

    correct_answer_index = randint(LOWER_LIMIT, limit)
    correct_answer = list[correct_answer_index]
    list[correct_answer_index] = ".."
    question = ' '.join(list)
    return question, correct_answer
