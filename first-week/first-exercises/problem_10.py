"""
Pedir tres números y mostrarlos ordenados de mayor a menor.
"""
n_1 = int(input("Write the first number: \n"))
n_2 = int(input("Write the second number: \n"))
n_3 = int(input("Write the third number: \n"))

ordered_numbers = [n_1, n_2, n_3]
ordered_numbers.sort(reverse=True)
print(f"Ordered numbers are: {ordered_numbers}")