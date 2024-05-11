#Limpar Terminal:
def Clean():
    import os
    sistema_operacional = os.name
    if sistema_operacional == 'posix':  # Para sistemas UNIX (Linux, macOS)
        os.system('clear')
    elif sistema_operacional == 'nt':  # Para Windows
        os.system('cls')

#Modulo:
def Module(num):
    try:
        if num < 0:
            return (num * -1)
        else:
            return num
    except:
        return "3RR0R!"

#Par Ou Impar:
def Par_Or_Impar(num):
    try:
        if num % 2 == 0:
            return True
        else:
            return False
    except:
        return "3RR0R!"
    
#Primo:
def Primo(num):
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
        return "3RR0R!"
    
#Fatorial:
def Factorial(num):
    try:
        if isinstance(num, int) == False or num < 0:
            return "3RR0R!"
        elif num == 0:
            return 1
        else:
            result = 1
            for i in range(num, 0, -1):
                result *= i
            return result
    except:
        return "3RR0R!"
    
#Exponenciação:
def Exp(base, exponent):
    try:
        return (base ** exponent)
    except:
        return "3RR0R!"
    
#Exponenciação:
def Exponentiation(base, exponent):
    try:
        result = 1
        if exponent > 0:
            for i in range(1, exponent + 1):
                result *= base
        elif exponent < 0:
            for i in range(1, (exponent * -1) + 1):
                result = (result / base)
        return result
    except:
        return "3RR0R!"

#Radiciação:
def Root(rooting, index):
    try:
        if index >= 0:
            return (rooting ** (1 / index))
        elif index == 0:
            if rooting == 1:
                return 1
            else:
                return "3RR0R!"
        elif index < 0:
            return (1 / (rooting ** (1 / (index * -1))))
        else:
            return "3RR0R!"
    except:
        return "3RR0R!"
    
#Delta:
def Delta(a, b, c):
    try:
        return ((b * b) - (4 * a * c))
    except:
        return "3RR0R!"

#Equação Do Segundo Grau:
def Bhaskara_And_Delta(a, b, c):
    try:
        delta = (b * b) - (4 * a * c)
        if delta > 0:
            return (((b * -1) + (delta ** (1 / 2))) / (2 * a)), (((b * -1) - (delta ** (1 / 2))) / (2 * a))
        elif delta == 0:
            return ((b * - 1) / (2 * a))
        else:
            return "3RR0R!"
    except:
        return "3RR0R!"

#Equação Do Segundo Grau:
def Bhaskara(a, b, delta):
    try:
        if delta > 0:
            return (((b * -1) + (delta ** (1 / 2))) / (2 * a)), (((b * -1) - (delta ** (1 / 2))) / (2 * a))
        elif delta == 0:
            return ((b * - 1) / (2 * a))
        else:
            return "3RR0R!"
    except:
        return "3RR0R!"
    
#Hipotenusa:
def Hypotenuse(cathetus1, cathetus2):
    try:
        return (((cathetus1 ** 2) + (cathetus2 ** 2)) ** (1 / 2))
    except:
        return "3RR0R!"
    
#Cateto:
def Cathetus(hypotenuse, cathetus):
    try:
        return (((hypotenuse ** 2) - (cathetus ** 2)) ** (1 / 2))
    except:
        return "3RR0R!"
    
#Circunferencia Com Raio:
def Circumference_R(radiu):
    try:
        return (3.141592653589793 * (radiu * 2))
    except:
        return "3RR0R!"
    
#Circunferencia Com Diametro:
def Circumference_D(diameter):
    try:
        return (3.141592653589793 * diameter)
    except:
        return "3RR0R!"
    
#Area De Um Circulo Pelo Raio:
def Circle_Area_R(radiu):
    try:
        return (3.141592653589793 * (radiu ** 2))
    except:
        return "3RR0R!"
    
#Area De Um Circulo Pelo Diametro:
def Circle_Area_D(diameter):
    try:
        return (3.141592653589793 * ((diameter / 2) ** 2))
    except:
        return "3RR0R!"
    
#Area De Um Circulo Pela Circunferencia:
def Circle_Area_D(Circumference):
    try:
        return ((Circumference / (2 * 3.141592653589793)) ** 2)
    except:
        return "3RR0R!"
    
#Area De Um Quadrado:
def Square_Area_D(base, altura):
    try:
        return (base * altura)
    except:
        return "3RR0R!"
    
#Area De Um Triangulo:
def Triangle_Area_D(base, altura):
    try:
        return ((base * altura) / 2)
    except:
        return "3RR0R!"