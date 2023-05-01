# f = open("pi.txt")
# print(f.read())

with open("pi.txt") as fayl:
    pi = fayl.read()
    print(pi)

# pi = pi.rstrip()  # qator ohiridagi bo'shliqlarni olib tashlaymiz
# pi = pi.replace("\n", "")  # qator tashlash belgisini almashtiramiz
# pi = float(pi)  # matnni float (o'nlik) songa o'tkazamiz
print(pi)

filename = "data/talabalar.txt"
with open(filename) as file:
    for line in file:
        print(line)

with open(filename) as file:
    talabalar = file.readlines()

print(talabalar)


talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)

faylnomi = "pi.txt"  # ochilayotgan (yaratilayotgan) fayl nomi
with open(faylnomi, "w") as fayl:
    fayl.write("Jasurbek,O'gabek,Javohir")  # faylga yozilayotgan ma'lumot


faylnomi = "new_file.txt"
ism = "Jasurbek Ergashev-"
tyil = 2002
with open(faylnomi, "w") as fayl:
    fayl.write(ism)
    fayl.write(str(tyil))

with open(faylnomi, "a") as fayl:
    fayl.write("\nAzizbek Murodov-")
    fayl.write("2003")

import pickle

talaba1 = {"ism": "hasan", "familiya": "husanov", "tyil": 2003, "kurs": 2}
talaba2 = {"ism": "alijon", "familiya": "valiyev", "tyil": 2004, "kurs": 1}

with open("info", "wb") as file:
    pickle.dump(talaba1, file)
    pickle.dump(talaba2, file)

with open("info", "rb") as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)

print(talaba1)
print(talaba2)
