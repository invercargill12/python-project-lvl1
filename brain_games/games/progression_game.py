from random import randint


def progression():
    list = []
    start = randint(1, 20)  # выбираем начальное число прогрессии
    step = randint(1, 10)  # выбираем рандомный шаг прогрессии
    end = start + (10 * step)  # выбираем конец прогрессии

    for index in range(start, end, step):
        list.append(str(index))

    limit = len(list) - 1

    correct_answer_index = randint(1, limit)
    correct_answer = list[correct_answer_index]
    list[correct_answer_index] = ".."
    question = (f'''What number is missing in the progression?
Question: {' '.join(list)}''')
    return question, correct_answer
