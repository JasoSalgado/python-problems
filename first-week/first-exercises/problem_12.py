"""
Pedir un número de entre 0 y 9.999 y mostrarlo con las cifras al revés.
"""
n_1 = int(input("Write a number: \n"))

reverse_numbers = ''.join(reversed(str(n_1)))
print(reverse_numbers)