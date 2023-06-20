import re


regex = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
# print(re.match(regex, tel_number))


while True:
    tel_number = input("Telefon raqamingizni kirting:")
    if re.match(regex, tel_number):
        print("Raqamingiz  qabul qilindi.Birozdan keyin siz bilan aloqaga chiqamiz.")
        break
    else:
        print("Kiritgan raqamingiz yaroqsiz.Boshqa kiriting.")
