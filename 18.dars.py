#Sana:28.12.2022 year
#Mavzu:While and lists,dictionary
#Muallif:Murodov Azizbek 
'''
products=[]
n=1
while True:
   question=f"Sizga kerak bo'lgan {n}-mahsulotni kiriting:"
   pro=input(question)
   products.append(pro)
   answer=input("Yana qo'shasizmi? (yes/no)")
   if answer=='yes':
    n+=1
    continue
   else:
     break
print("Bozorliq:"+products)    
'''  

products={}
n=1
sum=0
while True:
   question=f"Sizga kerak bo'lgan {n}-mahsulotni kiriting:"
   pro=input(question)
   price=input(f"{pro}ning narhini kiriting:")
   products[pro]=int(price)
   sum+=int(price)
   answer=input("Yana qo'shasizmi? (yes/no)")
   if answer=='yes':
    n+=1
    continue
   else:
     break
print(products)    
print(sum)
    