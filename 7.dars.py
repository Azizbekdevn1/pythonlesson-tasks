##Mavzu :Lists practs
##Sana:19.11.2022 year
##Muallif:Azizbek Murodov
davlatlar=["O'zbekiston","Ukraina","Rossiya","Dubai","AQSH","Ispaniya"]
print(davlatlar)
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar,reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
sonlar=list(range(120,1201,2))
print(sonlar)
print(len(sonlar))
print(max(sonlar))
print(min(sonlar))
print(sum(sonlar))
print(max(sonlar)-min(sonlar))
boshi=sonlar[0:20]
orta=sonlar[270:291]
oxiri=sonlar[521:541]
print(boshi)
print(orta)
print(oxiri)
taomlar=['Norin','Osh','Manti','Kabob','Shashlik']
nonushta=taomlar[:]
nonushta.append('Tort')
nonushta.remove('Osh')
print(nonushta)
print(taomlar)
nonushta=tuple(nonushta)
print(nonushta)
nonushta=list(nonushta)
print(nonushta)
nonushta[0]='qaymoq va non'
print(nonushta)