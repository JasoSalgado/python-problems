"""
Pedir un número entre 0 y 9.999, decir si es capicúa.
"""

n_1 = int(input("Write a number: \n"))

if n_1 >= 0:
    if str(n_1) == str(n_1)[::-1]:
        print(f"{n_1} is a palindromic number")
    else:
        print(f"{n_1} is not a palindromic number")

