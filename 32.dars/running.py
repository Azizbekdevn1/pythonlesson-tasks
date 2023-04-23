from classes import Student,Subjects




student1=Student("Azizbek","Murodov","AC2296068",1)
student2=Student("Ergashev ","Khujaqul","AB3254113",2)
student3=Student("Ruslan","Rizayev","AC1234567",4)
student4=Student("To'rayev","Og'abek","AC9367237",3)
student5=Student("Ergashev ","Jasurbek","AP3254113",4)
student6=Student("Salohiddinov","Akbarali","AC1287567",2)
print(student1==student2)
print(student2<=student3)
print(student1>student3)
algebra=Subjects("Algebra va sonlar nazariyasi",5)
mantiq=Subjects("Diskret matematika va matemati mantiq",6)
analiz=Subjects("Matematik Analiz",5)
russian=Subjects("Rus tili",4)
program=Subjects("Dasturlash asoslari",6)  
algoritm=Subjects("Linked lists",6)  
algebra.add_students(student1,student2,student5)
program.add_students(student3,student4,student6)
print(len(algebra))
print(len(program))
print(len(russian))
print(algebra[2])
print(program[1])
student7=Student("Qo'yliyev","Ruslan","BG3276908",2)
algebra[0]=student7
print(algebra[2])
print(algebra[:])
print(program[:])
student8=Student("Quvvatov","Mirmuhsin","JH73827294",2)
student9=Student("John","Arnold","JH73827294",6)
program+student8
algebra+student8
print(algebra[:])
print(program[:])
new_subject=program+algebra
print(new_subject[:])
#program-student6
#print(program[:])
#new_subject1=program-algebra
#print(new_subject1[:])
algebra(student9)
print(algebra())
