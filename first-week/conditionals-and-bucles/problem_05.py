"""
Realizar un juego para adivinar un número. Para ello pedir un número N, y luego ir pidiendo números indicando “mayor” o “menor” según sea mayor o menor con respecto a N. El proceso termina cuando el usuario acierta.
"""
# Library
import random
print("***** Guess the number *****")
print("\n")

random_number = random.randint(1, 50)
entered_number = int(input("Write a number from 1 to 50: \n"))

while entered_number != random_number:
    if entered_number < random_number:
        print("Write a higher number, please. \n")
    else:
        print("Write a smaller number, please. \n")
    entered_number = int(input("Write another number: "))
print(f"The {entered_number} is the winner")