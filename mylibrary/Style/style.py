def Write(phrase: str, timing: float = 0.1):
    """
    Write a phrase in the console with a delay between each character.

    Parameters:
    - phrase: The phrase to be written in the console.
    - timing: The delay between each character in seconds (default: 0.1).
    """
    from sys import stdout
    from time import sleep
    phrase = phrase.strip()
    for i in phrase:
        sleep(timing)
        print(i, end='')
        stdout.flush()