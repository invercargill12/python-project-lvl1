#!/usr/bin/env/python

import prompt
from brain_games.logic.even_logic import is_even

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    is_even()

if __name__ == '__main__':
    main()
