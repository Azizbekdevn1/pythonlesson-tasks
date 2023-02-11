#Lists -ro'yhat
#9.11.2022 yil



#mevalar=['anor','olma','shaftoli','tarvuz']
#print(mevalar[0])
#print(mevalar[3])
#mevalar[2]='nok'
#print(mevalar)
#mevalar.append("qovun")
#mevalar.append("xurmo")
#mevalar.append("uzum")
#print(mevalar)
#mevalar.insert(2,"apelsin")
#print(mevalar)
#del mevalar[4]

names = ['Jurabek', 'Jasur', 'Firdavs', 'Akbarali']
print(names[0] + " yaxshimisan jura O'qishlaring yaxshimi")
print(names[1] + " qachon bir munday uchrashamiz " + names[3] +
      "ni ham chaqirsak yaxshi bulardi a nima deysan")
print("Jasur: Bo'ldi jurala gap yo'q shanba kuni bo'shman ")
sonlar = [12, -1234, 23.4, -7463289, 23, 3.14256717, 2.71345]
sonlar.append(4483)
sonlar.append(4.73636)
sonlar[5] = 54
sonlar[3] = 'butun'
print(sonlar)
del sonlar[1]
print(sonlar)
sonlar.remove('butun')
print(sonlar)
subject = ['math', 'english', 'russian', 'programming', 'history']
bugun = subject.pop(3)
print("Bugun bizga " + bugun + " darsi o'tilmadi ")
t_shaxslar = ['A.Temur', 'Beruniy', 'I.Karimov', "Cho'lpon", "...."]
z_shaxslar = ['Elon Musk', 'Jack Ma ', 'Khabib', 'Darhonbek']
ta = t_shaxslar.pop(3)
za = z_shaxslar.pop(0)
print("Men tarixiy shaxslardan " + ta + " bilan " +
      " zamonaviy shaxslardan esa " + za +
      " bilan suhbatlashishni hoxlar edim .")
freinds = ['Jasur', 'Jurabek', "Og'abek", 'Kamron', 'Alibek', 'Jonibek']
print(freinds)
freinds.append('Akbarali')
freinds.append('Vorisbek')
freinds.append('Firdavs')
freinds.append('Javohir')
print(freinds)
freinds.remove('Jasur')
freinds.remove('Alibek')
freinds.remove('Javohir')
print(freinds)
mehmonlar = []
mehmonlar.append(freinds.pop(1))
mehmonlar.append(freinds.pop(4))
mehmonlar.append(freinds.pop(2))
mehmonlar.append(freinds.pop(1))
print("Kelgan mehmonlar " + str(mehmonlar))
