#Muallif:Azizbek Murodov
#Sana:02.01.2023 year
#Mavzu:Qiymat  qaytaruvchi funksiya 
'''
def infor_mation(name,surname,t_yili,t_joyi,email=None,raqam=None):

    mijoz={'ismi':name,
                'familiya':surname,
                 'tugilgan yili':t_yili,
                 'tugilgan joyi':t_joyi,
                 'emaili':email,
                 'yoshi':(2022-t_yili),
                 'raqami':raqam}

    return mijoz 
  
mijoz1=infor_mation('Azizbek','Murodov',2003,
                   'Qashqadaryo','murodovazizbek330@gmail.com',
                   998912112143)  
mijoz2=infor_mation('Jasurbek','Ergashev'
                   ,2003,'Toshkent')

mijozlar=[mijoz1,mijoz2]
for mijoz in mijozlar: 
  if mijoz['raqami'] or mijoz['emaili']:
    raqam=mijoz['raqami']
    email=mijoz['emaili']
  else :
    raqam="noma'lum"
    email="noma'lum"
    
  print(f"\n{mijoz['familiya']} {mijoz['ismi']} "
  f"{mijoz['yoshi']}  yoshda"
  f".elektron pochtasi {email},{mijoz['tugilgan yili']} yilda"  
  f" tug'ilgan, tel raqami {raqam}")

print("Tashrif buyurgan mijozlarni ma'lumotlarini yig'ib lug'at ko'rinishida chop qilamiz:")
def infor_mation(name,surname,tyili,tjoyi,email,yosh,raqam):

    mijoz={     'name':name,
                'surname':surname,
                 'tyili':tyili,
                 'tjoyi':tjoyi,
                 'email':email,
                 'yosh':yosh,
                 'telraqam':raqam}

    return mijoz 
mijozlar=[]
while True:
  print("\n Quyidagi ma'lumotlarni kiriting:")
  name=input("Ismizngiz nima: ")
  surname=input("Familyangiz nima: ")
  tyil=input("Qachon tug'ilgansiz: ")
  tjoyi=input("Qayerda tug'ilgansiz: ")
  email=input("Elektron pochtangizni kiriting: ")
  yosh=input("Necha yoshdasiz: ")
  telraqam=input("Tel raqamingizni kiriting: ")

  
  mijozlar.append(infor_mation(name,surname,
                               tyil,tjoyi,email,yosh,telraqam))
  javob=input("Keyingisi bormi ? (yes/no): ")
  if javob=='no':
     break
for mijoz in mijozlar:
  print(f"\n{mijoz['surname']}, {mijoz['name']}"
  f"{mijoz['yosh']}  yoshda"
  f".elektron pochtasi {mijoz['email']},{mijoz['tyili']} yilda"  
  f" tug'ilgan, tel raqami {mijoz['telraqam']} ")
  '''
#print("3 ta son qabul qilib ulardan eng kattasini qabul qiluvchi funksiya yozamiz :")
#def three(a,b,c):
 # if a>b and a>c:
  #  print(f"Eng kattasi: {a}")
     
# elif b>a and b>c:
 #   print(f"Eng kattasi: {b}")
     
 # elif c>a and c>b:
  #  print(f"Eng kattasi: {c}")
     
    
#three(3,64,-43)
#three(-23423,343,33443)
#def aylana_info(radius,pi=3.14214):
#  aylana={
 #         'radius':radius,
 #         'diametr':2*radius,
  #        'uzunligi':2*pi*radius,
 #         'yuzi ':pi*(radius**2),
    
  #        }
 # return aylana

#aylana_info(3)
#print(aylana_info(4))

#def tub_sonlar_top(min, max):
 #   tub_sonlar = []
 #   for n in range(min, max + 1):
  #      tub = True
  #      if n == 1:
 #           tub = False
 #       elif n == 2:
 #           tub = True
 #       else:
  #          for x in range(2, n):
  #              if n % x == 0:
  #                  tub = Fals
   #     if tub:
   #         tub_sonlar.append(n)

   # return tub_sonlar

#print(tub_sonlar_top(3,29))
#print(tub_sonlar_top(1,432))
def fibo(n):
    sonlar=[]
    for x in range(n):
        if x==0 or x==1:
           sonlar.append(1)
        else:
           sonlar.append(sonlar[x-1]+sonlar[x-2])

    return sonlar
 
print(fibo(21))    



