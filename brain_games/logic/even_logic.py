from random import randint
import prompt


def is_even():
    random_number = randint(1, 200)
    print(f'Question: {random_number}')
    answer_select = prompt.string('Your answer: ')
    print(answer_select)
    index = 0
    winscore = 3
    congrats = print('Congratulations, {name}!')
    while index < winscore:
        if random_number % 2 == 0 and answer_select.lower() == 'yes':
            print('Correct!')
            index = index + 1
        elif random_number % 2 != 0 and answer_select.lower() == 'yes':
            return print('''"yes" is wrong answer ;(. Correct answer was "no".
Let's try again, {name}''')
        elif random_number % 2 == 0 and answer_select.lower() == 'no':
            return print('''"no" is wrong answer ;(. Correct answer was "yes".
Let's try again, {name}''')
        elif random_number % 2 != 0 and answer.lower() == 'no':
            return print('''"no" is wrong answer ;(. Correct answer was "yes".
Let's try again, {name}''')
    return congrats

