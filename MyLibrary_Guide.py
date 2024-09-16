# MyLibrary Documentation



# -Python-Library-Import-
import MyLibrary  # Note: The library file must already be in the folder where your file is located.


# -Clear-the-Terminal-Function-
MyLibrary.Clean()  # Clearing the terminal


# -Check-If-A-Variable-Is-A-Valid-Number-Function-
value = '2'  # Variable to be checked. Note: it is recommended to use variables of type str, but it also works perfectly with variables of type int and float.
print(MyLibrary.Verify.Number(value))  # Checking whether or not the variable is a valid number. If it is a valid number, the function returns True, if it is not a valid number, the function returns False.


# -Check-If-A-Number-Is-Even-Function-
number = 4  # Number to be checked.
print(MyLibrary.Verify.Pair(number))  # Checking if the number is even. Returns True if it is even, otherwise False.


# -Check-If-A-Number-Is-Prime-Function-
number = 7  # Number to be checked.
print(MyLibrary.Verify.Prime(number))  # Checking if the number is prime. Returns True if it is prime, otherwise False.


# -Validate-CPF-Function-
cpf = '12345678901'  # CPF to be validated.
print(MyLibrary.CPF(cpf))  # Validates if the given CPF number is valid. Returns True if it is valid, otherwise False.


# -Calculate-Factorial-Function-
num = 5  # Number to calculate the factorial.
print(MyLibrary.Factorial(num))  # Calculates the factorial of the given number.


# -Calculate-Root-Function-
number = 16  # Number to calculate the root of.
index = 2  # Index of the root.
print(MyLibrary.Root(number, index))  # Calculates the square root or nth root of the number.


# -Calculate-Delta-of-Quadratic-Equation-Function-
a, b, c = 1, -3, 2  # Coefficients of the quadratic equation.
print(MyLibrary.Delta(a, b, c))  # Calculates the delta (discriminant) of the quadratic equation.


# -Use-Bhaskara's-Formula-Without-Delta-Function-
a, b, c = 1, -3, 2  # Coefficients of the quadratic equation.
print(MyLibrary.Bhaskara.NoDelta(a, b, c))  # Finds the solutions to a quadratic equation using Bhaskara's formula without delta.


# -Use-Bhaskara's-Formula-With-Delta-Function-
a, b, delta = 1, -3, 1  # Coefficients of the quadratic equation and delta value.
print(MyLibrary.Bhaskara.WithDelta(a, b, delta))  # Finds the solutions to a quadratic equation using Bhaskara's formula with delta.


# -Calculate-Hypotenuse-of-Triangle-Function-
cathetus1, cathetus2 = 3, 4  # Lengths of the two catheti.
print(MyLibrary.Hypotenuse(cathetus1, cathetus2))  # Calculates the hypotenuse of a right triangle.


# -Calculate-Cathetus-of-Triangle-Function-
hypotenuse, cathetus = 5, 3  # Hypotenuse and one cathetus.
print(MyLibrary.Cathetus(hypotenuse, cathetus))  # Calculates the length of the remaining cathetus.


# -Calculate-Circumference-of-Circle-Using-Radiu-Function-
radius = 5  # Radius of the circle.
print(MyLibrary.Circumference.WithRadius(radius))  # Calculates the circumference of a circle using its radius.


# -Calculate-Circumference-of-Circle-Using-Diameter-Function-
diameter = 10  # Diameter of the circle.
print(MyLibrary.Circumference.WithDiameter(diameter))  # Calculates the circumference of a circle using its diameter.


# -Calculate-Area-of-Shapes-Functions-

# Circle area by radius
radius = 5  # Radius of the circle.
print(MyLibrary.Area.Circle.Radius(radius))  # Calculates the area of a circle using its radius.


# Circle area by diameter
diameter = 10  # Diameter of the circle.
print(MyLibrary.Area.Circle.Diameter(diameter))  # Calculates the area of a circle using its diameter.


# Circle area by circumference
circumference = 31.41592653589793  # Circumference of the circle.
print(MyLibrary.Area.Circle.Circumference(circumference))  # Calculates the area of a circle using its circumference.


# Square area
base, height = 4, 5  # Base and height of the square.
print(MyLibrary.Area.Square(base, height))  # Calculates the area of a square.


# Triangle area
base, height = 4, 5  # Base and height of the triangle.
print(MyLibrary.Area.Triangle(base, height))  # Calculates the area of a triangle.


# -Convert-Temperature-Function-
temperature = 25  # Temperature value.
current_unit = "°C"  # Current unit of temperature.
target_unit = "°F"  # Target unit of temperature.
print(MyLibrary.ConvertTemperature(temperature, current_unit, target_unit))  # Converts temperature from one unit to another.


# -Calculate-Compound-Interest-Using-Decimal-Tax-Functions-
capital = 1000  # Initial capital.
tax = 0.05  # Interest rate in decimal.
time = 2  # Time period in years.
print(MyLibrary.Interest.Denary(capital, tax, time))  # Calculates compound interest with tax in decimal form.


# -Calculate-Compound-Interest-Using-Percentage-Tax-Functions-
capital = 1000  # Initial capital.
tax_percentage = 5  # Interest rate in percentage.
time = 2  # Time period in years.
print(MyLibrary.Interest.Percentage(capital, tax_percentage, time))  # Calculates compound interest with tax in percentage form.


# -Generate-Random-Key-Function-
length = 10  # Length of the random key.
print(MyLibrary.GenerateKey(length))  # Generates a random sequence of characters with the specified length.