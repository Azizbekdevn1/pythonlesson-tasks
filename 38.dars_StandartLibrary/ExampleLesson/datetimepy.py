import datetime as dt

hozir = dt.datetime.now()
print(hozir)
# sanani ajratib olish
print(hozir.date())

# vaqtni ajratib olish
print(hozir.time())

# soatni ajratib olish
print(hozir.hour)

# minutni ajratib olish
print(hozir.minute)

# sekundni ajratib olish
print(hozir.second)

bugun = dt.date.today()
print(f"Bugungi sana: {bugun}")
ertaga = dt.date(2023, 6, 20)
print(f"Ertangi sana: {ertaga}")


hozir = dt.datetime.now()
vaqtHozir = hozir.time()
print(f"Hozir soat: {vaqtHozir}")

vaqtKeyin = dt.time(23, 45, 00)
bugun = dt.date.today()
ramazon = dt.date(2023, 7, 28)
farq = ramazon - bugun
print(farq)
print(f"Ramazonga {farq.days} kun qoldi")


hozir = dt.datetime.now()
futbol = dt.datetime(2023, 4, 13, 23, 45, 00)
farq = futbol - hozir
sekundlar = farq.seconds
minutlar = int(sekundlar / 60)
soatlar = int(minutlar / 60)
print(f"Futbol boshlanishiga {sekundlar} sekund qoldi")
print(f"Futbol boshlanishiga {minutlar} minut qoldi")
print(f"Futbol boshlanishiga {soatlar} soat qoldi")

# vaqtni millisekundsiz chiqaramiz
vaqt = hozir.strftime("%H:%M:%S")
print(f"Hozir soat: {vaqt}")

# sanani kun-oy-yil koʻrinishida chiqaramiz
sana = hozir.strftime("%d-%m-%Y")
print(f"Bugun sana: {sana}")

# sanani kun/oy/yil koʻrinishida chiqaramiz
sana_vaqt = hozir.strftime("%d/%m/%Y, %H:%M")
print(sana_vaqt)
