"""
16. Pide un número (que debe estar entre 0 y 10) y mostrar la tabla de multiplicar de dicho número.
"""

n = int(input("Write a number: \n"))
for x in range(11):
    print(f"{n} * {x} =", n * x)