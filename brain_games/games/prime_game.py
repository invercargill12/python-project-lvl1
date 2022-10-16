from random import randint


RANGE_START = 2
RANGE_STEP = 1
LOWER_LIMIT = 1
UPPER_LIMIT = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(random_number):

    if random_number < 2:
        return False

    for i in range(RANGE_START, random_number, RANGE_STEP):
        if random_number % i == 0:
            return False

    return True


def get_round_data():
    random_number = randint(LOWER_LIMIT, UPPER_LIMIT)

    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = random_number
    return question, correct_answer
