#Sana:07.05.2023 year
#Mavzu:Exceptions
#Muallif:Murodov Azizbek

import json
number=input("Telifon raqamingizni kiriting:")
try:
     number=int(number)
     print(f"Telifon raqamingiz:{number}")
except:
     print("Siz raqamingizni kiritmadingiz:")


yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh)    
except ValueError:
    print("Butun son kiritmadingiz")
else:
    print(f"Siz {2023-yosh} yilda tug'ilgansiz")


x,y=5,10
try:
   y/(x-5)
except ZeroDivisionError:
    print("0 ga bo'lib bo'lmaydi")
    
mevalar = ['olma','anor','anjir','uzum']
try:
    print(mevalar[7])
except IndexError:
    print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")
    
    
    user = {"username":"sariqdev",
        "status":"admin",
        "email":"admin@sariq.dev",
        "phone":"99897123456"}

key="tel"
try:
    print(f'Foydalanuvchi: {user[key]}')
except KeyError:
    print("Bunday kalit mavjud emas")
    
filename = "data.txt" # bunday fayl mavjud emas
try:
    with open(filename) as f:
        text = f.read()
except FileNotFoundError:
    print(f"Kechirasiz, {filename} fayli mavjud emas. Bosh fayl tanlang.")
    
    
n = input("Butun son kiriting: ")
try:
    n = int(n)
    x=20/n
except ValueError: # agar foydalanuvchi butun son kiritmasa
    print("Butun son kiritmadingiz")
except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa
    print("0 ga bo'lib bo'lmaydi")
else:
     print(f"x={x}")
     
while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break        

print(f"Siz {2021-yosh} yilda tug'ilgansiz")