# Sana 19.06.2023
# Mavzu:Standart library
# Muallif:Murodov Azizbek

import datetime as dt

# bugun = dt.date.today()
## print(f"Bugun:{bugun}")
## print(f"Bugun:{farq-bugun}")
# for i in range(0, 12):
#    day = bugun.day + 14
#    month = bugun.month + int(day / 30)
#    year = bugun.year + int(month / 12)
#    if day > 30 or month > 13:
#        month = month - 12
#        day = day - 30
#    bugun = dt.date(year, month, day)
#    print(bugun)


# Get today's date
today = dt.date.today()

# Output 10 dates, 2 weeks apart from today
for i in range(20):
    date = today + dt.timedelta(weeks=2 * i)
    print(date)
