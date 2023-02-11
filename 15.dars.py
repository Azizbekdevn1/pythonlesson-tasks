#Mavzu:Lug'at elementlari bilan ishlash
#Sana:25.12.2022 year
#Muallif:Azizbek Murodov

print("1-semestr davomida o'tilgan fanlar ro'yhati:")
subjects={'mathematical logic':['matematik mantiq', 6]
          ,'number theory':['algebra va sonalar nazariyasi',5]
          ,'recent history':["o'zbekistonning eng yangi tarixi",4]
          ,'mathematical analysis':['matematik analiz',4]
          ,'fundamentals of programming':['dasturlash asoslari',6]
          ,'english':['ingiliz tili',5]}
print("Dunyo davlatlati:          Davlatlarning poytaxtlari:")       
for key,value in sorted(subjects.items()):
  print(f"{key.title()}-{value}\n")


states={'Aqsh':'Washington',
         "O'zbekiston":'Tashkent',
         'Rossiya':'Moskva',
        'Singapur':'Singapur',
         'Tojikiston':'DSushanbe',
         "Qozog'iston":'Nursulton',
         'Italiya':'Rim',
         'Malayziya':'Kuala-lumpur',
         "Qirg'iziston":'Bishkek'
        }
print ("Dunyo davlatlari:")
for davlat in sorted(states):
  print(davlat.upper())

print("\nDavlatlarning poytaxtlari:")
for poytaxt in sorted(states.values()):
  print(poytaxt.title())
  
capital=input("Qaysi davlatning poytaxtini bilishni xohlaysiz?:").lower()
print(states.get(capital,"Kechirasiz bizda u haqida ma'lumot yo'q"))  
menu={'osh':20000,'shashlik':14000,"sho'rva":22000,'norin':75000,"nohotshorak":24000,"lagman":21000}
savat=[]
print("3 ta taom buyurtma bering:")
narh=0
for i in range(1,4):
   savat.append(input(f"{i}-taom:").lower())     
for taom in savat:
   if taom in menu:
    narh=narh+int(menu[taom])
    print(f"{taom.title()} {menu[taom]} so'm")
     
   else:
    print(f"Kechirasiz, bizda {taom} yo'q")
print(f"Sizdan {narh} so'm bo'ldi")