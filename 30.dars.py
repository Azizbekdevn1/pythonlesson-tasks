#Sana:28.01.2023 year
#Muallif:Murodov Azizbek
#Mavzu:Vorislik va polimorfizm





class Subjects():
    def __init__(self,name):
        """Fanni yaratuvchi klass"""
        self.name=name 
        
    def get_subject_name(self):
        return f"{self.name} "
    
class Student():
    def __init__(self,name,surname,pasport,kurs):
        """Talaba haqida malumotni qaytaruvchi funksiya """
        self.name=name
        self.surname=surname
        self.pasport=pasport
        self.kurs=kurs
        self.subjects=[]
        self.number=0
        
    def get_info(self):
        return f"{self.name} {self.surname} {self.kurs}-kurs talabasi."
    
    def add_subjects(self,subject):
         self.subjects.append(subject)
         self.number+=1
         return self.subjects
     
    def set_subjects(self):
        return self.number
        
     
    def get_subjects_info(self):
        return [subject.get_subject_name() for subject in self.subjects]
     
     
    def remove_subject(self,sub):
        if sub in self.subjects:
            self.subjects.remove(sub)
            self.number-=1
            return self.subjects
        else:
            print(f"Bu fandan sizdan imtixon olinmaydi.")
            
        

        
algebra=Subjects("Algebra va sonlar nazariyasi")
mantiq=Subjects("Diskret matematika va matematik mantiq")
analiz=Subjects("Matematik Analiz")
russian=Subjects("Rus tili")
program=Subjects("Dasturlash asoslari")  
algoritm=Subjects("Linked lists")  
student=Student("Azizbek","Murodov","AC2296068",1)
print(student.get_info())
student.add_subjects(algebra)
print(student.get_subjects_info())
student.add_subjects(mantiq)
print(student.get_subjects_info())
student.add_subjects(analiz)
student.add_subjects(russian)
student.add_subjects(program)
print(student.get_subjects_info())
print(student.set_subjects())
student.remove_subject(algebra)
print(student.get_subjects_info())
print(student.set_subjects())
student.remove_subject(program)
print(student.get_subjects_info())
student.remove_subject(algoritm)
print(student.get_subjects_info())
student.remove_subject(russian)
print(student.get_subjects_info())
print(student.set_subjects())
student.remove_subject(analiz)
print(student.get_subjects_info())
student.remove_subject(mantiq)
print(student.get_subjects_info())
print(student.set_subjects())


         
         
         






