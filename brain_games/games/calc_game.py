from random import randint
from random import choice


def calc():
    operator = choice(['*', '+', '-'])
    num_one = randint(1, 30)
    num_two = randint(1, 10)
    question = (f'''What is the result of the expression?
Question: {num_one} {operator} {num_two}''')
    correct_answer = str(eval(f'{num_one}{operator}{num_two}'))
    return question, correct_answer


