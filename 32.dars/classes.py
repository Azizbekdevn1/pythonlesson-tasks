#Muallif:Murodov Azizbek
#Sana:22.04.2023 
#Mavzu: Dunder metodlar

class Subjects():
    __sum_kridet=0
    __sum_subjects=0
    def __init__(self,name,kridet=5):
        """Fanni yaratuvchi klass"""
        self.name=name 
        self.__kridet=kridet
        self.talabalar=[]
        Subjects.__sum_kridet+=kridet
        Subjects.__sum_subjects+=1
        
    def get_subject_name(self):
        return f"{self.name} "
    def get_kridet(self):
        return self.__kridet
    #With dunder metods
    def add_students(self,*value):
     for student in value:
          if isinstance(student,Student):
               self.talabalar.append(student)
          else:
               print("Student obektini kiriting:")
               
    def sub_students(self,*value):
     for student in value:
          if isinstance(student,Student):
               self.talabalar.pop(student)
          else:
               print("Student obektini kiriting:")
    def __len__(self):
        return len(self.talabalar)
   
    def __getitem__(self,index):
        return self.talabalar[index]
   
    def __setitem__(self,index,value1):
        if isinstance(value1,Student):
            self.talabalar[index]=value1    
            
    def __add__(self,qiymat):
        if isinstance(qiymat,Subjects):
            yangi_fan =Subjects(f"{self.name} {qiymat.name}")
            yangi_fan.talabalar = self.talabalar + qiymat.talabalar
            return yangi_fan
        elif isinstance(qiymat,Student):
             self.add_students(qiymat)
        else:
             print(f"Fanga {type(qiymat)} qo'shib bo'lmaydi:")

    def __sub__(self,remove):
        if isinstance(remove,Student):
             self.sub_students(remove)
        else:
             print(f"Fanga {type(remove)} qo'shib bo'lmaydi:")

    def __call__(self):
        return [student for student in self.talabalar]
          # Yuqoridagi obyektlarni fanga ga qo'shamiz
          
    def __call__(self,*param):
        if param: # agar parametr bo'lsa
            for student in param:
                self.add_students(student)
        else: # agar parametr bo'lmasa
            return [student for student in self.talabalar]
    @classmethod
    def get_sum_kridet(cls):
        return cls.__sum_kridet
    def get_sum_subjects(cls):
        return cls.__sum_subjects 
    
    
   
    
class Student():
    """Student classi"""
    __num_student=0
    def __init__(self,name,surname,pasport,kurs):
        """Talaba haqida malumotni qaytaruvchi funksiya """
        self.name=name
        self.surname=surname
        self.pasport=pasport
        self.kurs=kurs
        self.subjects=[]
        self.number=0
        Student.__num_student+=1
     
    @classmethod
    def get__num_student(cls):
        return cls.__num_student
    
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
            
     #With dunder metods
    def __repr__(self):
         return f"{self.name} {self.surname} {self.kurs}-kurs talabasi."
    
    def __eq__(self,other_student):
        """Tenglik"""
        return self.kurs == other_student.kurs
    
    def __lt__(self,other_student):
        """Kichik"""
        return self.kurs<other_student.kurs
    
    def __le__(self,other_student):
        """Kichik yoki teng"""
        return self.kurs<=other_student.kurs
            
