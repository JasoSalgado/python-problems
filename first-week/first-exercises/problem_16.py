"""
Pedir el día, mes y año de una fecha e indicar si la fecha es correcta. Con meses de 28, 30 y 31 días. Sin años bisiestos.
"""

instructions = "***** Enter a valid date. For instance: dd/mm/yyyy *****"
print(instructions.center(50, "*"))

day = int(input("Write a day: \n"))
month = int(input("Write a month: \n"))
year = int(input("Write a year: \n"))

if year == 0:
    print(f"This {year} does not exist.")
else:
    if month == 2 and day >= 1 and day <= 28:
        print(f"This {month} does not have the day you entered")
    else:
        if month ==1 or month == 3 or month == 7 or month == 8 or month == 10 or month == 12 and day >= 1 and day <= 31:
            print(f"{day}/{month}/{year} is a correct date.")
        else:
            print(f"{day}/{month}/{year} is an incorrect date. Try again, please.")
        

