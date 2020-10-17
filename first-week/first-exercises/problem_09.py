"""
Pedir dos números y mostrarlos ordenador de mayor a menor
"""
n_1 = int(input("Write a number: \n"))
n_2 = int(input("Write another number: \n"))

ordered_numbers = [n_1, n_2]
ordered_numbers.sort(reverse=True)
print(f"Ordered numbers: {ordered_numbers}")
