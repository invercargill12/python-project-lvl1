from random import randint


def is_even():
    random_number = randint(1, 200)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = (f'''Answer "yes" if the number is even, otherwise answer "no".
Question: {random_number}''')
    return question, correct_answer
