from random import randint


LOWER_LIMIT = 1
START_UPPER_LIMIT = 20
STEP_UPPER_LIMIT = 10
MIN_LENGTH = 5
MAX_LENGTH = 12
DESCRIPTION = 'What number is missing in the progression?'


def get_progression(start, step, length):
    end = start + (length * step)
    numbers_list = []
    for index in range(start, end, step):
        numbers_list.append(index)
    return numbers_list


def get_round_data():
    start = randint(LOWER_LIMIT, START_UPPER_LIMIT)
    step = randint(LOWER_LIMIT, STEP_UPPER_LIMIT)
    length = randint(MIN_LENGTH, MAX_LENGTH)
    progression = get_progression(start, step, length)
    correct_answer_index = randint(LOWER_LIMIT, len(progression) - 1)
    correct_answer = str(progression[correct_answer_index])
    progression[correct_answer_index] = ".."
    question = ' '.join(map(str, progression))
    return question, correct_answer
