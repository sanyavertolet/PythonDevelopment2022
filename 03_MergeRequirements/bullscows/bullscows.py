import textdistance
def bullscows(guess: str, secret: str) -> (int, int):
    bulls = textdistance.levenshtein.similarity(guess, secret)
    cows = textdistance.bag.similarity(guess, secret)
    return bulls, cows

if __name__ == '__main__':
    print(bullscows('ропот', 'полип'))
