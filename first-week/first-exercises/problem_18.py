"""
Ídem que el ej. 17, suponiendo que cada mes tiene un número distinto de días (suponer que febrero tiene siempre 28 días).
"""

instructions = "***** Enter a valid date. For instance: dd/mm/yyyy *****"
print(instructions.center(50, "*"))

day = int(input("Write a day: \n"))
month = int(input("Write a month: \n"))
year = int(input("Write a year: \n"))

def next_date(year, month, day):
    
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_days = 31
    elif month == 2:
        month_days = 28
    else:
        month_days = 30

    if day < month_days:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    
    return (year, month, day)

print(next_date(year, month, day))