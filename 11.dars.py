#Mavzu:Dictionary-Lug'atlar 
# Sana:24.12.2022 year
#Muallif:Azizbek Murodov

me={'gender':'erkak','age':'19','uneversity':"O'zMu",'course':'1'}
print(f"Salom.Mening ismim Azizbek.Men {me['age']} yoshdaman.Men {me['uneversity']} da {me['course']} bosqich talabasiman.")
ota={'name':'Muhammadqul'\
     ,'t_yil':'1958'\
     ,'region':'Kashkadaryo '\
     ,'district':'Kitob'}
print(f"Mening otamning ismi {ota['name']},{ota['t_yil']}-yilda,{ota['region']} viloyati {ota['district']} tumanida tavvallud topganlar.")
ona={'name':'Saboxat'\
     ,'t_yil':'1960'\
     ,'region':'Kashkadaryo '\
     ,'district':'Kitob'}
print(f"Mening onamning ismi {ona['name']},{ona['t_yil']}-yilda,{ona['region']} viloyati {ona['district']} tumanida tavvallud topganlar.")
aka={'name':'Laziz'\
     ,'t_yil':'1990'\
     ,'region':'Kashkadaryo '\
     ,'district':'Kitob'}
print(f"Mening akamning ismi {aka['name']},{aka['t_yil']}-yilda,{aka['region']} viloyati {aka['district']} tumanida tavvallud topganlar.")

food={'fries':'qovurilgan kartoshka','plov':'osh','manti':'manti','lagman':'lag\'mon','dumpling':'chuchvara'}
food['fried fish']='qovurilgan baliq'
print(f"Mening sevimli yaxshi ko'radigan ovqatim {food['fries']}")
print(f"Akamning sevimli yaxshi ko'radigan ovqati {food['dumpling']}")
print (f"Onamning sevimli yaxshi ko'radigan ovqati {food['fried fish']}")
python={'int':'butun son','float':'haqiqiy son','string':'matn','if':'agar','else':'aks holda'}
son=input(" Kalit so'zni kiriting>>")

if son in python:
  print(python[son])
else:
  print("mavjud emas")

key=python[son]
print(key)
print(python.get(son,"Bunday qiymat mavjud emas:"))
del python['else']
print(python)