from random import randint


LOWER_LIMIT = 1
UPPER_LIMIT = 200
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_round_data():
    random_number = randint(LOWER_LIMIT, UPPER_LIMIT)
    if is_even(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = random_number
    return question, correct_answer


def is_even(random_number):
    return random_number % 2 == 0
