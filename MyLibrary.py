def Clean():
    """This function clears the terminal."""
    from os import name, system
    os_system = name
    if os_system == 'posix': 
        system('clear')
    elif os_system == 'nt':  
        system('cls')


class Verify:
    def Number(var: str): 
        """This function checks if a variable is a number."""

        digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".")
        for i in str(var):
            if i not in digits:
                return False
        return True

    
    def Pair(num: int): 
        """This function checks if a number is even."""

        try:
            if num % 2 == 0:
                return True
            else:
                return False
        except:
            return 'ERROR!'
        
    
    def Prime(num: int): 
        """This function checks if a number is prime."""

        try:
            x = 0
            for i in range(1, num + 1):
                if num % i == 0:
                    x += 1
                if x > 2:
                    break
            if x == 2:
                return True
            else:
                return False
        except:
            return 'ERROR!'

    
    def CPF(cpf):
        """This function checks if an eleven-digit sequence is a valid CPF."""
        
        cpf_digits = []
        try:
            for i in range(0, 11):
                cpf_digits.append(int(cpf[i]))
            if len(cpf_digits) != 11:
                return False
            else:
                x1 = ((cpf_digits[0] * 10) + (cpf_digits[1] * 9) + (cpf_digits[2] * 8) + (cpf_digits[3] * 7) + (cpf_digits[4] * 6) + (cpf_digits[5] * 5) + (cpf_digits[6] * 4) + (cpf_digits[7] * 3) + (cpf_digits[8] * 2)) % 11
                if x1 < 2:
                    d1 = 0
                else:
                    d1 = 11 - x1
                if cpf_digits[9] != d1:
                    return False
                else:
                    x2 = ((cpf_digits[0] * 11) + (cpf_digits[1] * 10) + (cpf_digits[2] * 9) + (cpf_digits[3] * 8) + (cpf_digits[4] * 7) + (cpf_digits[5] * 6) + (cpf_digits[6] * 5) + (cpf_digits[7] * 4) + (cpf_digits[8] * 3) + (cpf_digits[9] * 2)) % 11
                    if x2 < 2:
                        d2 = 0
                    else:
                        d2 = 11 - x2
                    if cpf_digits[10] != d2:
                        return False
                    else:
                        return True
        except:
            return 'ERROR!'



def Factorial(num: float):
    """This function calculates the factorial of a number."""

    try:
        if (not isinstance(num, int) and not num.is_integer()) or num < 0:
            return 'ERROR!'
        elif num == 0:
            return 1
        else:
            num = int(num)
            result = 1
            for i in range(num, 0, -1):
                result *= i
            return result
    except:
        return 'ERROR!'
    

def Root(rooting: float, index: float):
    """This function calculates the root of a number."""

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
    """This function calculates the delta of a quadratic equation. \n
    Formula: b² - 4.a.c"""
    try:
        return ((b * b) - (4 * a * c))
    except:
        return 'ERROR!'


class Bhaskara:
    def NoDelta(a: float, b: float, c: float):
        """This function calculates the X of a quadratic equation along with the delta of that same quadratic equation. \n
        Formulas: (-b + √(b² - 4.a.c)) / (2.a) | (-b - √(b² - 4.a.c)) / (2.a)"""

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
        """This function calculates the X of a quadratic equation. \n
        Formulas: (-b + √Δ) / (2.a) | (-b - √Δ) / (2.a)"""

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
    """This function calculates the hypotenuse of a right-angled triangle. \n
    Formula: √(Ca² + Cb²)"""

    try:
        return (((cathetus1 ** 2) + (cathetus2 ** 2)) ** (1 / 2))
    except:
        return 'ERROR!'
    

def Cathetus(hypotenuse: float, cathetus: float):
    """This function calculates the cathetus of a right-angled triangle. \n 
    Formula: √(H² - C²)"""

    try:
        return (((hypotenuse ** 2) - (cathetus ** 2)) ** (1 / 2))
    except:
        return 'ERROR!'
    

class Circumference:
    def WithRadius(radius: float):
        """This function calculates the circumference of a circle using its radius. \n
        Formula: 2.r.π"""

        try:
            return (3.141592653589793 * (radius * 2))
        except:
            return 'ERROR!'
        

    def WithDiameter(diameter: float):
        """This function calculates the circumference of a circle using its diameter. \n
        Formula: d.π"""

        try:
            return (3.141592653589793 * diameter)
        except:
            return 'ERROR!'



class Area:
    class Circle:
        def Radius(radius: float):
            """This function calculates the area of a circle using its radius. \n
            Formula: r².π"""

            try:
                return (3.141592653589793 * (radius ** 2))
            except:
                return 'ERROR!'
        
        
        def Diameter(diameter: float):
            """This function calculates the area of a circle using its diameter. \n
            Formula: (d/2)².π"""

            try:
                return (3.141592653589793 * ((diameter / 2) ** 2))
            except:
                return 'ERROR!'
        
        
        def Circumference(circumference: float): 
            """This function calculates the area of a circle using its circumference. \n
            Formula: Not Remembered"""

            try:
                return ((circumference / (2 * 3.141592653589793)) ** 2)
            except:
                return 'ERROR!'


    def Square(base: float, height: float):
        """This function calculates the area of a square. \n
        Formula: b.h"""

        try:
            return (base * height)
        except:
            return 'ERROR!'


    def Triangle(base: float, height: float):
        """This function calculates the area of a triangle. \n
        Formula: (b.h) / 2"""

        try:
            return ((base * height) / 2)
        except:
            return 'ERROR!'



def ConvertTemperature(temperature: float, current_unit: str, target_unit: str):
    """This function converts temperature between °C, °F, or K. \n
        Formulas: \n 
        °C = ((°F - 32) / 9) * 5 | °C = K - 273.15 \n
        °F = ((°C / 5) * 9) + 32 | °F = (((K - 273.15) / 5) * 9) + 32 \n
        K = °C + 273.15 | K = (((°F - 32) / 9) * 5) + 273.15"""
    
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
        """This function calculates compound interest with the rate in decimal form. \n
        Formula: c.(1 + i)ᵗ"""

        try:
            return capital * ((1 + tax) ** time)
        except:
            return 'ERROR!'

    
    def Percentage(capital: float, tax: float, time: float):
        """This function calculates compound interest with the rate in percentage form. \n
        Formula: c.(1 + (i / 100))ᵗ"""

        try:
            return capital * ((1 + (tax / 100)) ** time)
        except:
            return 'ERROR!'



def GenerateKey(length: int, char_list: list = None):
    """This function generates a random sequence of characters from a provided list or a default list, with a defined length. \n
        Default List: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '|', ';', ':', ',', '<', '.', '>', '/', '?', '~', '`']"""
    try:
        from random import choice
        if length <= 0:
            return 'ERROR!'
        if not char_list:
            char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '|', ';', ':', ',', '<', '.', '>', '/', '?', '~', '`']
        return ''.join(choice(char_list) for _ in range(length))
    except:
        return 'ERROR!'
