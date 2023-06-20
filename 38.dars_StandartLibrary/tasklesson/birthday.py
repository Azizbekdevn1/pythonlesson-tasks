import datetime as dt

bugun = dt.date.today()
birthday = dt.date(2003, 7, 17)
print(type(birthday))
print(f"Tug'ilgan kunimgacha {bugun-birthday} kun qoldi ")


def Findays(year, month, day):
    distance = bugun - dt.date(year, month, day)
    kun = distance.days
    month = int(kun / 30)
    year = int(month / 12)
    print(f"Tug'ilganimga {year} yil   bo'ldi.")
    print(f"Tug'ilganimga {month}  oy bo'ldi.")
    print(f"Tug'ilganimga {kun}  kun bo'ldi.")


Findays(2003, 7, 17)
