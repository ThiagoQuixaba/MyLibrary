def Number(var: str):
    """
    Checks if a variable is a number.

    Parameters:
    - var (str): The variable to be checked.

    Returns:
    - bool: True if the variable is a number, False otherwise.
    """
    digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".")
    for i in str(var):
        if i not in digits:
            return False
    return True

def Pair(num: int):
    """
    Checks if a number is even.

    Parameters:
    - num (int): The number to be checked.

    Returns:
    - bool: True if the number is even, False otherwise.
    """
    try:
        return num % 2 == 0
    except:
        return 'ERROR!'

def Prime(num: int):
    """
    Checks if a number is prime.

    Parameters:
    - num (int): The number to be checked.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    try:
        x = 0
        for i in range(1, num + 1):
            if num % i == 0:
                x += 1
            if x > 2:
                break
        return x == 2
    except:
        return 'ERROR!'

def CPF(cpf: str):
    """
    Checks if an eleven-digit sequence is a valid CPF.

    Parameters:
    - CPF (str): The CPF number as a string (000.000.000-00).

    Returns:
    - bool: True if the CPF is valid, False otherwise.
    """
    from re import match
    
    if not all(c.isdigit() or c in '.-' for c in cpf):
        return False
    if not (match(r'^\d{11}$', cpf) or match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf)):
        return False
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or all(digit == cpf[0] for digit in cpf):
        return False
    try:
        x1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
        d1 = 0 if x1 % 11 < 2 else 11 - (x1 % 11)
        if int(cpf[9]) != d1:
            return False
        x2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
        d2 = 0 if x2 % 11 < 2 else 11 - (x2 % 11)
        if int(cpf[10]) != d2:
            return False
        return True
    except:
        return 'ERROR!'
    
def PhoneNumber(phone: str) -> bool:
    """
    Checks if a phone number is valid based on various formats.

    Parameters:
    - phone (str): The phone number as a string.

    Returns:
    - bool: True if the phone is valid, False otherwise.
    """
    from re import match

    if not all(c.isdigit() or c in '+()- ' for c in phone):
        return False
    formatos = [
        r'^\+\d{2} \(\d{2}\) \d{5}-\d{4}$',
        r'^\+\d{2} \(\d{2}\) \d{4}-\d{4}$',
        r'^\+\d{2} \d{2} \d{5}-\d{4}$',
        r'^\+\d{2} \d{2} \d{4}-\d{4}$',
        r'^\d{2} \d{2} \d{5}-\d{4}$',
        r'^\d{2} \d{2} \d{4}-\d{4}$',
        r'^\+\d{2} \(\d{2}\) \d{9}$',
        r'^\+\d{2} \(\d{2}\) \d{8}$',
        r'^\+\d{2} \d{2} \d{9}$',
        r'^\+\d{2} \d{2} \d{8}$',
        r'^\d{2} \d{2} \d{9}$',
        r'^\d{2} \d{2} \d{8}$',
        r'^\d{13}$',
        r'^\d{12}$',
    ]
    for formato in formatos:
        if match(formato, phone):
            return True
    return False