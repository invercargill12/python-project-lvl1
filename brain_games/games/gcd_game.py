import math
from random import randint


def common_divisor():
    num_one = randint(2, 100)
    num_two = randint(2, 100)
    question = (f'''Find the greatest common divisor of given numbers.
Question: {num_one} {num_two}''')
    correct_answer = str(math.gcd(num_one, num_two))
    return question, correct_answer
