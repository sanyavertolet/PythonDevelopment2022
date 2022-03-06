from bullscows import bullscows

import random

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret_word = random.choice(words)
    guess_word = ''
    counter = 0
    while secret_word != guess_word:
        guess_word = ask('Введите слово: ', words)
        counter += 1
        bulls, cows = bullscows(guess_word, secret_word)
        inform('Быки: {}, Коровы: {}', bulls, cows)
    return counter
    
