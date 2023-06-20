import datetime as dt

bugun = dt.date.today()
ramazon = dt.date(2023, 6, 28)
hayit = dt.date(2023, 4, 15)
print(f"Ramazon o'tganiga {int(bugun.day-hayit.day)} kun boldi ")
print(f"Hayitgacha  {ramazon.day-bugun.day}kun qoldi")
