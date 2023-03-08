
from  classname   import Student,Subjects



        
algebra=Subjects("Algebra va sonlar nazariyasi",5)
mantiq=Subjects("Diskret matematika va matemati mantiq",6)
analiz=Subjects("Matematik Analiz",5)
russian=Subjects("Rus tili",4)
program=Subjects("Dasturlash asoslari",6)  
algoritm=Subjects("Linked lists",6)  
student=Student("Azizbek","Murodov","AC2296068",1)
print(Student.get__num_student())
Professor=Student("Erkin","Normatov","Ab34632",4)
print(student.get_info())
student.add_subjects(algebra)
print(student.get_subjects_info())
student.add_subjects(mantiq)
print(student.get_subjects_info())
print(mantiq.get_kridet())
print(algoritm.get_sum_kridet())
print(algoritm.get_sum_subjects())

