from random import randint


def progression():
    my_list = []
    start = randint(1, 20)  # выбираем начальное число прогрессии
    step = randint(1, 10)  # выбираем рандомный шаг прогрессии
    end = start + (10 * step)  # выбираем конец прогрессии
    for index in range(start, end, step):
        my_list.append(index)

    limit = len(my_list) - 1

    correct_answer_index = randint(1, limit)
    correct_answer = str(my_list[correct_answer_index])
    my_list[correct_answer_index] = '..'
    question = (f'''What number is missing in the progression?
Question: {my_list}''')
    return question, correct_answer
