# Sana:1.05.2023
# Mavzu:Fayllar bilan ishlash
# Muallif:Murodov Azizbek
import pickle

with open("learn_today.txt") as file:
    read = file.read()
    print(read)


with open("pi_million_digits.txt") as file:
    pi = file.read()
    date = "07172003"
    print(date in pi)
    pi = pi.rstrip()  # qator ohiridagi bo'shliqlarni olib tashlaymiz
    pi = pi.replace("\n", "")  # qator tashlash belgisini almashtiramiz
    pi = pi.replace(" ", "")
#   print(pi)


with open("float_pivalue", "wb") as file:
    pickle.dump(pi, file)


with open("float_pivalue", "rb") as file:
    pickle.load(file)

# print(pi)
while True:
    food = input("Yoqtirgan taomlaringizni kiriting (to'xtash uchun enterni bosing):")
    if not food:
        break
    with open("food.txt", "a") as file:
        file.write(food + "\n")
