#Sana:18.01.2023 year
#Muallif:Murodov Azizbek
#Mavzu:Obektlar bilan ishlash
'''class Avto():
     def __init__(self,model,rang,karobka,narh,motor):
          self.model=model
          self.rang=rang
          self.karobka=karobka
          self.narh=narh
          self.motor=motor
          self.kilometr=0
          
          
     def get_info(self):
          #Obyektning xusussiyatlari haqida ma'lumot  beradigan funksiya 
          
          return f"{self.rang} rangli {self.model}  avtomobili {self.karobka} karobkali {self.motor} ot kuchiga ega narhi {self.narh} yangi ya'ni {self.kilometr} km  yurgan"
     def get_model(self):
          return f"{self.model} ni GM ishlab chiqarishdan to'xtatdi."
     def get_color(self):
          return f"{self.rang} rangli moshinalarni sotuvi odatda yaxshi bo'ladi"
     def get_karobka(self):
          return f"{self.karobka} karobkali moshinalarni katta tezlikka chiqishi ko'p vaqt oladi" 
     def get_price(self):
          return f"{self.narh} Sizningcha GM moshinalari sifatiga yarasha  {self.narh} narhga arziydimi?"
     def update_km(self,go):
  
          self.kilometr+=go
     
avto1=Avto("Nexia 2","qora","mexanika","7000$", "1.6 litr")
print(avto1.get_info())
print(avto1.get_model())
print(avto1.get_color())
print(avto1.get_karobka())
print(avto1.get_price())
print(avto1.update_km(400))
print(avto1.get_info())
print(avto1.update_km(400))
print(avto1.get_info())'''

class Avtosalon():
     def __init__(self,dealership,address,carsforsale,):
          self.dealership=dealership
          self.address=address
          self.carsforsale=carsforsale
          self.many=3000
          self.cars=[]
          self.number=0
          self.wallet=0
     def get_info(self):
          #Avtosalon haqida umumiy ma'lumot 
          return f"{self.dealership} Saloning asosiy office {self.address}da joylashgan bo'lib,asosan {self.carsforsale} brandlariga tegishli moshinalar {self.many} ta avtoulov sig'dira oladi  "



     def add_cars(self,car,price):
          #Avtomobil qo'shamiz 
         
          self.cars.append(car)
          self.number+=1
          self.wallet+=price
          return f"Siz sotib olgan moshinalar {self.number} ta :{self.cars}  Jami:{self.wallet}$"
     
     def see_methods(klass):
          return [method for method in dir(klass) if method.startswith('__') is False]


avtosalon1=Avtosalon("BMW","Germaniya Berlin shahri","Rolls Royse,BMW,Mercedens Benz,Kia,Hyundai")
print(avtosalon1.get_info())
print(avtosalon1.add_cars('BMW x7',150000))
print(avtosalon1.add_cars('Mercedens Benz Gelik',500000))
print(avtosalon1.add_cars('Malibu 2 turbo',40000))
print(avtosalon1.add_cars('Tahoe',90000))
print(avtosalon1.add_cars('Lamborghini',1000000))
print(dir(Avtosalon))
print(avtosalon1.__dict__)
print(avtosalon1.__format__)









