"""
Pedir dos números y decir cual es el mayor o si son iguales.
"""

n_1 = int(input("Write a number: \n"))
n_2 = int(input("Write another number: \n"))

if n_1 > n_2:
    print(f"{n_1} is higher than {n_2}")
elif n_1 == n_2:
    print(f"{n_1} are the same {n_2}")
else:
    print(f"{n_1} is less than {n_2}")
