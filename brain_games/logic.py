def logic(game):
    question, correct_answer, random_number = game()
    # шаг 1: поздороваться
    print('Welcome to the Brain Games!')
    # шаг 2: спросить имя
    name = prompt.string('May I have your name? ')
    # шаг 3: поздороваться + имя
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    # шаг 4: задает вопрос нужной игры
    index = 0
    score = 3
    while index < score:
        print(question)
        # шаг 5: читает ответ
        answer = prompt.string('Your answer: ')
        # шаг 6: сравнение ответа с правильным
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f'Let\'s try again, {name}!')
            return
        # шаг 7: увеличивается кол-во очков (если верно) - переход в след раунд
        index = index + 1
        # шаг 8: игра завершается
    print(f'Congratulations, {name}!')
