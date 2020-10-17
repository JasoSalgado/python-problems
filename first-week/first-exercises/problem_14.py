"""
Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien...
"""

grade = int(input("Write a grade from 0 to 10: \n"))

if grade >= 0 and grade <= 5:
    print("Insufficient")
elif grade >= 6 and grade <= 7:
    print("Sufficient")
elif grade >= 8 and grade <= 10:
    print("Very well")
else:
    print("You entered a wrong number")