"""
Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene.
"""
n_1 = int(input("Write a number from 0 to 9.999: \n"))
counter = len(str(n_1))

print(f"The number you entered has: {counter}")