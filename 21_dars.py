#Muallif:murodov Azizbek
#Sana:3.01.2023 year
#Mavzu:Funksiya va ro'yhatlar

#def katta_harf(matnlar):
#    matnlar=matnlar[:]
#    for i in range(len(ismlar)):
#        matnlar[i]=matnlar[i].title()
#    return matnlar 
#ismlar=['ali','azizbek','jasurbek','akbarali','jurabek']
#katta_harf(ismlar)
#yangi_ismlar=katta_harf(ismlar)
#print(ismlar)
#print(yangi_ismlar)

talabalar = ["ali", "vali", "hasan", "husan"]


def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar


baholar = bahola(talabalar)
print(baholar)
print(talabalar)
