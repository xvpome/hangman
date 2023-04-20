def leapMonth(month, year):
    def leapYear():
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                 return False
            else:
                return True
        else:
            return False
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leapYear():
        month_days[1] = 29
    return (month_days[month-1])

year = int(input("Year: "))
month = int(input("Month: "))
print(leapMonth(month, year))

