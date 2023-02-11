#Mavzu: IF-else
#Sana:20/11/2022
#Muallif:Azizbek Murodov 

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car!='gm':
    print(car.title())
  else: 
    print(car.upper())

for car in cars:
  if car=='gm':
    print(car.upper())
  else: 
    print(car.title())


log=input("Xurmatli foydalanuvchi loginingizni kiriting >>")
if log=='Admin':
  print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
  print("Xush kelibsiz," +log)

a=float(input('a sonni kiriting:'))
b=float(input('b sonni kiriting:'))
if a==b:
  print("a va b sonlari o'zaro teng")
else:
  print('Sonlar bir-biriga teng emas')

son=float(input("Ixtiyoriy sonni kiriting :"))
if son>=0 :
  print('Bu son musbat   son')
else:
  print('Bu son manfiy  son')

s=int(input('Son kiriting:'))
if s>=0 :
  print("Bu sondan kvadrat ildiz:"+str(s**(1/2)))
else:
  print("Musbat son kiriting:")