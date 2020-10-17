"""
Pedir dos fechas y mostrar el número de días que hay de diferencia. Suponiendo todos los meses de 30 días.
"""

# Library
from datetime import datetime

instructions = "***** Enter a valid date. For instance: mm/dd/yyyy *****"
print(instructions.center(50, "*"))

def difference_in_days():

    format = "%d/%m/%Y"

    while True:
        try:
            today = input("Write today´s date: \n")
            if today == "":
                break

            another_day = input("Write another date: \n")
            if another_day == "":
                break

            today = datetime.strptime(today, format)
            another_day = datetime.strptime(another_day, format)

            if another_day >= today:
                difference = another_day - today
                print(f"The difference of days are: {difference.days} \n")
                break
            else:
                print("The last date must be higher than the first one")
        except:
            print("Error:")

if __name__ == "__main__":
    difference_in_days()
