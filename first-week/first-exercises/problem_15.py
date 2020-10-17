"""
Pedir el día, mes y año de una fecha e indicar si la fecha es correcta. 
Suponiendo que todos los meses son de 30 días.
"""
# Library
from datetime import datetime

instructions = "***** Enter a valid date. For instance: dd/mm/yyyy *****"
print(instructions.center(50, "*"))

while True:
    entered_date = input("Enter a valid date: \n")
    try:
        date = datetime.strptime(entered_date, "%d/%m/%Y")
    except ValueError:
        print("The date you entered is incorrect")
    else:
        break
