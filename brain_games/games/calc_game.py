from random import randint
from random import choice

LOWER_LIMIT = 1
UPPER_LIMIT = 30
DESCRIPTION = 'What is the result of the expression?'


def get_round_data():
    operator = choice(['*', '+', '-'])
    num_one = randint(LOWER_LIMIT, UPPER_LIMIT)
    num_two = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = f'{num_one} {operator} {num_two}'
    correct_answer = str(sum_counter(num_one, operator, num_two))
    return question, correct_answer


def sum_counter(num_one, operator, num_two):
    if operator == '*':
        result = num_one * num_two
    elif operator == '+':
        result = num_one + num_two
    elif operator == '-':
        result = num_one - num_two
    return result
