from random import randint
import prompt


def is_even():
    random_number = randint(1, 200)
    question = (f'Question: {random_number}')
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer

