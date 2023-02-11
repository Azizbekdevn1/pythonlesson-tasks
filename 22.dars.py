#Muallif:Murodov Azizbek
#    Sana:7.01,2022 year
#Mavzu:Moslashuvchan funksiya
'''
def multipli(*numbers):
    #Kiritilgan barcha sonlarni ko'paytmasini hisoblovchi funksiya 
    mult=1
    for number in numbers:
        mult*=number
    return mult
    

print(multipli(2,4,5,6,7,8,9))
print(multipli(-3,-5,4.5,6,7.8,-3))
print(multipli(1,2,3,4,5,6,7,8,9,10))
'''
#def student_info(name,surname,**information):
#    #Talabdan o'zi haqida ma'lumot oluvhci funksiya
#    information['name']=name
#    information['surname']=surname
#    return information
#
#student_1=student_info('Azizbek','Murodov',tyili=2003,yoshi=20,kasbi='Dasturchi')
#student_2=student_info('Akbarali','Salohiddinov',ojoyi='TATU',hobby='PUBG',t_joyi='Qashqadaryo')
#print(student_1)
#print(student_2)






