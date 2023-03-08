#Muallif:Murodov Azizbek
#Sana:8.03.2023 
#Mavzu: INKAPSULYATSIYA


class Subjects():
    __sum_kridet=0
    __sum_subjects=0
    def __init__(self,name,kridet=5):
        """Fanni yaratuvchi klass"""
        self.name=name 
        self.__kridet=kridet
        Subjects.__sum_kridet+=kridet
        Subjects.__sum_subjects+=1
        
    def get_subject_name(self):
        return f"{self.name} "
    def get_kridet(self):
        return self.__kridet
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
            
