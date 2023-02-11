#Mavzu:For loop
#Muallif:Azizbek 
#Sana:19.11.2022 year
names=['Jurabek','Jasur','Azizbek','Ogabek','Suxrob']
for ism  in names:
  print(ism)
print("Kod "+str(len(names))+" marta takrorlandi.")

t_sonlar=list(range(11,100,2))
print(t_sonlar)
for son in t_sonlar:
  print(f"{son}ning kubi {son*son*son}ga teng")

kinolar=[]
print('Siz yoqtirgan va sevib tomosha qilgan 5 ta kinolar')
for n in range(1,6):
  kinolar.append(input(f"{n}-kino:"))
print(kinolar)

  
suxbat=[]
soni=int(input("Bugun nechchi kishi bilan suhbat qildingiz>>"))
for soni in range(soni) :
  suxbat.append(input(f"{soni+1}-suhbat qilgan odam kim edi: "))
print(suxbat)