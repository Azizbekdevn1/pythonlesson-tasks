import re

# matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
# Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
# 👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
# 👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

# andoza = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
# email = re.findall(andoza, matn)
# print(email)
#
## Kuchli parolni tekshirish
## Quyidagi andoza ham ihateregex.io sahifasidan olindi
# andoza = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$"
# msg = "Yangi parol kiriting"
# msg += "(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, "
# msg += "1 ta son va 1 ta maxsus belgi boʻlishi kerak): "
#
# while True:
#    password = input(msg)
#    if re.match(andoza, password):
#        print("Maxfiy so'z qabul qilindi")
#        break
#    else:
#        print("Maxfiy so'z talabga javob bermadi")


word1 = "salom"
word2 = "sariq"
word3 = "salim"


regex = "^s...m$"


print(re.match(regex, word1))
print(re.match(regex, word2))
print(re.match(regex, word3))
