from random import randint


def is_prime(random_number):
    for i in range(2, random_number, 1):
        if random_number % i == 0 or random_number == 1:
            return False
    return True


def prime_number_check():
    random_number = randint(1, 100)
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = (f'''Answer "yes" if given number is prime. Otherwise answer "no".
Question: {random_number}''')
    return question, correct_answer
