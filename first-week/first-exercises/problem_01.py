"""
Pedir los coeficientes de una ecuación de 2º grado, y muestre sus soluciones reales. Si no existen, debe indicarlo.

Having into account that the formula of the quadratic equation is:
ax**2 + bx + c = 0
"""

# Library
from math import sqrt

a = int(input("Write the quadratic term: \n"))
b = int(input("Write the linear term: \n"))
c = int(input("Write the independent term: \n"))

if ((b**2) - 4*a*c) < 0:
    print("This solution is only possible with complex numbers. \n")
else:
    x1 = (-b + sqrt(b**2-(4*a*c))) / (2*a) 
    x2 = (-b - sqrt(b**2-(4*a*c))) / (2*a)
    title = " The solution is: "
    print(title.center(30, "#"))
    print(f"x1: {x1}")
    print(f"x2: {x2}")