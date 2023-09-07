#Muallif:Murodov Azizbek 
#Sana:8.01.2023 year
#Mavzu :So'z topish o'yini
#Find game in Python


import random
def sontop(x=10):
     tasodifson=random.randint(1,x)
     print(f"1 dan {x} gacha son o'yladim topa olasizmi:")
     print("Let's go >>")
     taxminlar=0
     while True:
          taxminlar+=1
          taxmin=int(input(">>>"))
          if taxmin<tasodifson:
               print("Xato. men o'ylagan son bundan kattaroq.Yana harakat qiling ")
          elif taxmin>tasodifson:
               print("Xato. men o'ylagan son bundan kichikroq.Yana harakat qiling ")
          else:
               break
     print(f"Tabriklaymiz men {tasodifson} sonini o'ylagandim .{taxminlar} ta urinish bilan topdingiz?")
     return taxminlar

def sontop_comp(x=10):
     input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing.Men topaman")
     quyi=1
     yuqori=x
     tahminlar=0
     while True:
          tahminlar+=1
          if quyi!=yuqori:
               tahmin=random.randint(quyi,yuqori)
          else:
               quyi=tahmin


          javob=input(f"Siz {tahmin} sonini o'yladingiz,to'g'ri (t) ,"
                         f"men o'ylagan son bundan kattaroq (+) yoki kichikroq (-)".lower())
          

          if javob=='-':
               yuqori=tahmin-1
          elif javob=='+':
               quyi=tahmin+1
          else :
               break
     print(f"Men topdim siz {tahmin} sonini o'ylagan ekansiz")
     print(f"Men {tahminlar} ta  tahmin bilan topdim.")
     return tahminlar

def play(x=10):
     yana=True
     while yana:
          tahminlar_user=sontop(x)
          tahminlar_comp=sontop_comp(x)
          if tahminlar_comp>tahminlar_user:
               print("Siz yutdiz?")
          elif tahminlar_user>tahminlar_comp:
               print("Men yutdim?")
          else:
               print("Durrang")
          yana=int(input("O'yinni davom ettirasizmi ?.Ha(1)/yoq(0)"))
          
print(play(10))
