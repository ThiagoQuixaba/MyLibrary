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


class Verify:
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



def Factorial(num: any):
    """
    Calculates the factorial of a number.

    Parameters:
    - num (float, int, or str): The number for which the factorial will be calculated. Must be non-negative and an integer.

    Returns:
    - int: The factorial of the number.
    - str: 'ERROR!' if the input is invalid.
    """
    try:
        if isinstance(num, str):
            num = float(num)
        if not isinstance(num, (int, float)) or num < 0 or (isinstance(num, float) and not num.is_integer()):
            return 'ERROR!'
        num = int(num)
        result = 1
        for i in range(1, num + 1):
            result *= i
        
        return result
    except:
        return 'ERROR!'


def Root(rooting: float, index: float):
    """
    Calculates the root of a number.

    Parameters:
    - rooting (float): The number to find the root of.
    - index (float): The degree of the root.

    Returns:
    - float: The calculated root.
    - str: 'ERROR!' if the input is invalid or the operation is undefined.
    """
    try:
        if index >= 0:
            return (rooting ** (1 / index))
        elif index == 0:
            if rooting == 1:
                return "Indeterminate"
            else:
                return 'ERROR!'
        elif index < 0:
            return (1 / (rooting ** (1 / (index * -1))))
        else:
            return 'ERROR!'
    except:
        return 'ERROR!'


def Delta(a: float, b: float, c: float):
    """
    Calculates the delta of a quadratic equation.

    Formula: b² - 4.a.c

    Parameters:
    - a (float): Coefficient of x².
    - b (float): Coefficient of x.
    - c (float): Constant term.

    Returns:
    - float: The value of delta.
    - str: 'ERROR!' if the input is invalid.
    """
    try:
        return ((b * b) - (4 * a * c))
    except:
        return 'ERROR!'


class Bhaskara:
    def NoDelta(a: float, b: float, c: float):
        """
        Calculates the roots (X) of a quadratic equation along with delta.

        Formulas:
        - (-b + √(b² - 4.a.c)) / (2.a)
        - (-b - √(b² - 4.a.c)) / (2.a)

        Parameters:
        - a (float): Coefficient of x².
        - b (float): Coefficient of x.
        - c (float): Constant term.

        Returns:
        - tuple: A tuple containing the two roots if delta > 0.
        - float: A single root if delta == 0.
        - str: 'ERROR!' if delta < 0 or the input is invalid.
        """
        try:
            delta = (b * b) - (4 * a * c)
            if delta > 0:
                return (((b * -1) + (delta ** (1 / 2))) / (2 * a)), (((b * -1) - (delta ** (1 / 2))) / (2 * a))
            elif delta == 0:
                return ((b * - 1) / (2 * a))
            else:
                return 'ERROR!'
        except:
            return 'ERROR!'

    def WithDelta(a: float, b: float, delta: float):
        """
        Calculates the roots (X) of a quadratic equation using delta.

        Formulas:
        - (-b + √Δ) / (2.a)
        - (-b - √Δ) / (2.a)

        Parameters:
        - a (float): Coefficient of x².
        - b (float): Coefficient of x.
        - delta (float): The value of delta.

        Returns:
        - tuple: A tuple containing the two roots if delta > 0.
        - float: A single root if delta == 0.
        - str: 'ERROR!' if delta < 0 or the input is invalid.
        """
        try:
            if delta > 0:
                return (((b * -1) + (delta ** (1 / 2))) / (2 * a)), (((b * -1) - (delta ** (1 / 2))) / (2 * a))
            elif delta == 0:
                return ((b * - 1) / (2 * a))
            else:
                return 'ERROR!'
        except:
            return 'ERROR!'



def Hypotenuse(cathetus1: float, cathetus2: float):
    """
    Calculates the hypotenuse of a right-angled triangle.

    Formula: √(Ca² + Cb²)

    Parameters:
    - cathetus1 (float): Length of the first cathetus.
    - cathetus2 (float): Length of the second cathetus.

    Returns:
    - float: The length of the hypotenuse.
    - str: 'ERROR!' if the input is invalid.
    """
    try:
        return (((cathetus1 ** 2) + (cathetus2 ** 2)) ** (1 / 2))
    except:
        return 'ERROR!'


def Cathetus(hypotenuse: float, cathetus: float):
    """
    Calculates the length of a cathetus of a right-angled triangle.

    Formula: √(H² - C²)

    Parameters:
    - hypotenuse (float): Length of the hypotenuse.
    - cathetus (float): Length of the other cathetus.

    Returns:
    - float: The length of the missing cathetus.
    - str: 'ERROR!' if the input is invalid.
    """
    try:
        return (((hypotenuse ** 2) - (cathetus ** 2)) ** (1 / 2))
    except:
        return 'ERROR!'


class Circumference:
    def WithRadius(radius: float):
        """
        Calculates the circumference of a circle using its radius.

        Formula: 2 * π * r

        Parameters:
        - radius (float): The radius of the circle.

        Returns:
        - float: The circumference of the circle.
        - str: 'ERROR!' if the input is invalid.
        """
        try:
            return (3.141592653589793 * (radius * 2))
        except:
            return 'ERROR!'

    def WithDiameter(diameter: float):
        """
        Calculates the circumference of a circle using its diameter.

        Formula: π * d

        Parameters:
        - diameter (float): The diameter of the circle.

        Returns:
        - float: The circumference of the circle.
        - str: 'ERROR!' if the input is invalid.
        """
        try:
            return (3.141592653589793 * diameter)
        except:
            return 'ERROR!'


class Area:
    class Circle:
        def Radius(radius: float):
            """
            Calculates the area of a circle using its radius.

            Formula: π * r²

            Parameters:
            - radius (float): The radius of the circle.

            Returns:
            - float: The area of the circle.
            - str: 'ERROR!' if the input is invalid.
            """
            try:
                return (3.141592653589793 * (radius ** 2))
            except:
                return 'ERROR!'

        def Diameter(diameter: float):
            """
            Calculates the area of a circle using its diameter.

            Formula: π * (d / 2)²

            Parameters:
            - diameter (float): The diameter of the circle.

            Returns:
            - float: The area of the circle.
            - str: 'ERROR!' if the input is invalid.
            """
            try:
                return (3.141592653589793 * ((diameter / 2) ** 2))
            except:
                return 'ERROR!'

        def Circumference(circumference: float):
            """
            Calculates the area of a circle using its circumference.

            Formula: (C / (2 * π))² * π

            Parameters:
            - circumference (float): The circumference of the circle.

            Returns:
            - float: The area of the circle.
            - str: 'ERROR!' if the input is invalid.
            """
            try:
                return ((circumference / (2 * 3.141592653589793)) ** 2) * 3.141592653589793
            except:
                return 'ERROR!'

    def Square(base: float, height: float):
        """
        Calculates the area of a square.

        Formula: b * h

        Parameters:
        - base (float): The base of the square.
        - height (float): The height of the square.

        Returns:
        - float: The area of the square.
        - str: 'ERROR!' if the input is invalid.
        """
        try:
            return (base * height)
        except:
            return 'ERROR!'

    def Triangle(base: float, height: float):
        """
        Calculates the area of a triangle.

        Formula: (b * h) / 2

        Parameters:
        - base (float): The base of the triangle.
        - height (float): The height of the triangle.

        Returns:
        - float: The area of the triangle.
        - str: 'ERROR!' if the input is invalid.
        """
        try:
            return ((base * height) / 2)
        except:
            return 'ERROR!'



def ConvertTemperature(temperature: float, current_unit: str, target_unit: str):
    """
    Converts temperature between °C, °F, or K.

    Formulas:
    - °C = ((°F - 32) / 9) * 5 | °C = K - 273.15
    - °F = ((°C / 5) * 9) + 32 | °F = (((K - 273.15) / 5) * 9) + 32
    - K = °C + 273.15 | K = (((°F - 32) / 9) * 5) + 273.15

    Parameters:
    - temperature (float): The temperature to convert.
    - current_unit (str): The current unit of the temperature ('°C', '°F', or 'K').
    - target_unit (str): The target unit for the conversion ('°C', '°F', or 'K').

    Returns:
    - float: The converted temperature.
    - str: 'ERROR!' if the input is invalid.
    """
    try:
        if current_unit == "°C":
            if target_unit == "°C":
                return temperature
            elif target_unit == "°F":
                return ((temperature / 5) * 9) + 32
            elif target_unit == "K":
                return temperature + 273.15
            else:
                return 'ERROR!'
        elif current_unit == "°F":
            if target_unit == "°F":
                return temperature
            elif target_unit == "°C":
                return ((temperature - 32) / 9) * 5
            elif target_unit == "K":
                return (((temperature - 32) / 9) * 5) + 273.15
            else:
                return 'ERROR!'
        elif current_unit == "K":
            if target_unit == "K":
                return temperature
            elif target_unit == "°C":
                return temperature - 273.15
            elif target_unit == "°F":
                return (((temperature - 273.15) / 5) * 9) + 32
            else:
                return 'ERROR!'
        else:
            return 'ERROR!'
    except:
        return 'ERROR!'


class Interest:
    def Denary(capital: float, tax: float, time: float):
        """
        Calculates compound interest with the rate in decimal form.

        Formula: c * (1 + i)ᵗ

        Parameters:
        - capital (float): The initial amount of money.
        - tax (float): The interest rate in decimal form (e.g., 0.05 for 5%).
        - time (float): The time period over which the interest is applied.

        Returns:
        - float: The total amount after applying compound interest.
        - str: 'ERROR!' if the input is invalid.
        """
        try:
            return capital * ((1 + tax) ** time)
        except:
            return 'ERROR!'

    def Percentage(capital: float, tax: float, time: float):
        """
        Calculates compound interest with the rate in percentage form.

        Formula: c * (1 + (i / 100))ᵗ

        Parameters:
        - capital (float): The initial amount of money.
        - tax (float): The interest rate in percentage form (e.g., 5 for 5%).
        - time (float): The time period over which the interest is applied.

        Returns:
        - float: The total amount after applying compound interest.
        - str: 'ERROR!' if the input is invalid.
        """
        try:
            return capital * ((1 + (tax / 100)) ** time)
        except:
            return 'ERROR!'



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
