def ask(prompt: str, valid: list[str] = None) -> str:
    if valid is not None:
        return input(prompt)
    guess_word = input(prompt)
    while guess_word not in valid:
        guess_word = input(prompt)
    return guess_word


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))

