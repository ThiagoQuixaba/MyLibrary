def Clean():
    """
    Clears the terminal.

    Parameters:
    - None
    """
    from os import name, system
    os_system = name
    if os_system == 'posix': 
        system('clear')
    elif os_system == 'nt':  
        system('cls')

def GenerateKey(length: int, char_list: list = None):
    """
    This function generates a random sequence of characters from a provided list or a default list, with a defined length.

    Parameters:
    - length (int): The length of the generated key. Must be greater than 0.
    - char_list (list): Optional. A list of characters to use for generating the key.
    If not provided, a default list is used.

    Default List:
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '|', ';', ':', ',', '<', '.', '>', '/', '?', '~', '`']

    Returns:
    - str: A randomly generated key with the specified length.
    - str: 'ERROR!' if the input is invalid.
    """
    try:
        from random import choice
        if length <= 0:
            return 'ERROR!'
        if not char_list:
            char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '|', ';', ':', ',', '<', '.', '>', '/', '?', '~', '`']
        return ''.join(choice(char_list) for _ in range(length))
    except:
        return 'ERROR!'

def RepeatUntil(action_code: str, condition_code: str):
    """
    Executes a block of code repeatedly until a condition is satisfied.

    Parameters:
    - action_code (str): Python code (as a string) to be executed repeatedly.
    - condition_code (str): Python code (as a string) that evaluates whether the repetition should stop.
    """
    while True:
        exec(action_code)
        if eval(condition_code):
            break