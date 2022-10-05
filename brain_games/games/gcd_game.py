import math
from random import randint


LOWER_LIMIT = 2
UPPER_LIMIT = 50
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_round_data():
    num_one = randint(LOWER_LIMIT, UPPER_LIMIT)
    num_two = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = f'{num_one} {num_two}'
    correct_answer = str(math.gcd(num_one, num_two))
    return question, correct_answer
