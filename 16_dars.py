
#Mavzu:Nesting(Ichma -ich ro'yhat yoki lug'atlar)

#Sana:27.12.2022 year

#Muallif:Murodov Azizbek
'''
stiv={'ism':'Stiv Jobs','tyil':1955,'vyil':2011,'tjoy':'Kaliforniya'}
qodiriy={'ism':'Abdulla Qodiriy','tyil':1894,'vyil':1938,'tjoy':'Toshkent'}
vohidov={'ism':'Erkin Vohidov','tyil':1936,'vyil':2016,'tjoy':"Farg'ona"}
navoiy={'ism':'Alisher Navoiy','tyil':1401,'vyil':1501,'tjoy':"Xirot"}

shaxslar=[stiv,qodiriy,vohidov,navoiy]
for shaxs in shaxslar:
  print(f"{shaxs['ism']} {shaxs['tyil']}-yilda {shaxs['tjoy']}da tavallud topganlar.{shaxs['vyil']-shaxs['tyil']} yil umr ko'rganlar") 

stiv={
             'ism':'Stiv Jobs',
             'tyil':1955,
             'vyil':2011,
             'tjoy':'Kaliforniya',
             'asarlar':[
                 'Apple',
                 'Iphone',
                 'ITunes',
                 'Ipad'],
  }

qodiriy={
                'ism':'Abdulla Qodiriy',
                'tyil':1894,
                'vyil':1938,
                'tjoy':'Toshkent',
                'asarlar':[
                    'Otgan kunlar',
                    'Mehrobdan chayon',
                    'Obid ketmon'],
           
   }

vohidov={
              'ism':'Erkin Vohidov',
              'tyil':1936,
              'vyil':2016,
              'tjoy':"Farg'ona",
              'asarlar':[
                  'Tong nafasi', 
                  'Qo\'shiqlarim sizga',
                  'O\'zbegim',
                  'Qiziquvchan Marmusa'],
   }

navoiy={
          'ism':'Alisher Navoiy',
          'tyil':1401,
           'vyil':1501,
           'tjoy':"Xirot",
           'asarlar':['Xamsa',
                      'Mahbub Al-Qulub',
                      'Lison ut-tayr',
                      'Sabba\' Sayyor'],
    }

shaxslar=[stiv,qodiriy,vohidov,navoiy]
for shaxs in shaxslar:
    ism=shaxs['ism']
    asarlar=shaxs['asarlar']
    print(f"\n{ism}ning maxshxur asarlari:")
    for asar in asarlar:
        print(asar)
kinolar={
          'ali':['Po\'lat odam','Qasoskorlar','Chegarasizlar'],
          'aziz':['Anakonda','Qochish rejasi','Parker'],
          'jasur':['Abdullajon','Hayot','Jek va loviya poyasi '],
          'og\'abek':['Yirtqich va maxluq','Uyda yolg\'iz','Rembo'],
          'javohir':['O\'rgimchak odam ','Qora pantera','To\'ylar muborak'],
 
 }

for ism,kinolar in kinolar.items():
    print(f'\n{ism.title()}ning sevimli yoqtirgan kinolari quiyidagilar:')
    for kino in kinolar:
        print(kino)
'''

davlatlar = {
    "o'zbekiston": {
        "poytaxt": "toshkent",
        "maydon": 448978,
        "aholi": 33_000_000,
        "pul birligi": "so'm",
    },
    "rossiya": {
        "poytaxt": "moskva",
        "maydon": 17_098_246,
        "aholi": 144_000_000,
        "pul birligi": "rubl",
    },
    "aqsh": {
        "poytaxt": "vashington",
        "maydon": 9_631_418,
        "aholi": 327_000_000,
        "pul birligi": "dollar",
    },
    "malayziya": {
        "poytaxt": "kuala-lumpur",
        "maydon": 329750,
        "aholi": 25_000_000,
        "pul birligi": "rinngit",
    },
}
'''
for davlat,info in davlatlar.items():
    if davlat.lower()=='aqsh':
       davlat=davlat.upper()
    else:
        davlat=davlat.capitalize()
        
    print(
            f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
            f"\nHududi:{info['maydon']} kv.km"
            f"\nAholisi:{info['aholi'] }"
            f"\nPul birligi:{info['pul birligi']} "


)
'''

davlat=input("Davlat nomini kiriting:").lower()
if davlat in davlatlar:
       info=davlatlar[davlat]
       print(
             f"\n{davlat.title()}ning poytaxti {info['poytaxt'].title()}"
             f"\nHududi:{info['maydon']} kv.km"
             f"\nAholisi:{info['aholi'] }"
             f"\nPul birligi:{info['pul birligi']} "

 )
else:
    print("Bizda bu davlat haqida ma'\lumot yetarli emas")










