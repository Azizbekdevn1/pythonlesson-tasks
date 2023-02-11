#Sana:14.01.2023 year
#Muallif:Murodov Azizbek
#Mavzu:Class


class User:
     def __init__(self,ism,foydalanuvchinomi,email,traqam):  
          #Foydalanuvchidann ma'lumot olamiz
          self.fullname=ism
          self.username=foydalanuvchinomi
          self.email=email
          self.number=traqam

     def get_email(self):
          return self.email
     def get_number(self):
          return self.number

     def get_info(self):
          print(f" Xush kelibsiz {self.username}.Hurmatli {self.fullname}" 
                f".Saytga kirish kodini {self.email} elektron pochtayizga va {self.number} telefon raqamingizga yubordik.")


student1=User("Azizbek Murodov","Janob Coder","azizbekmurodov2003@gmail.com",+912112143)
student2=User("Jasurbek Ergashev","Jasurtech","jasurbektech283@gmail.com",+998944112143)
student3=User("Akbarali Salohiddinov","Nomard","akisalohiddinov343@gmail.com",+998952112143)
print(student1.get_info())
print(student2.get_info())
print(student3.get_info())

print(student1.get_email())
print(student2.get_number())


