from fuzzywuzzy import fuzz
print(fuzz.ratio("salom",'assalom'))
print(fuzz.ratio("salom","salim"))
print(fuzz.ratio("Azizbek","Murodov"))
