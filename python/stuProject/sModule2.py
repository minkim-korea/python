class Student:
   count =1  
   def __init__(self,name,kor,eng,math):
        self.no = Student.count       # 인스턴스변수
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math 
        self.avg = (kor+eng+math)/3  
        self.rank = 0 
        Student.count += 1           # 1증가
        
   def __str__(self):
        return f"""{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"""
    
class Students:
   def __init__(self):
        self.students = []
    
   def add(self,s):
        self.students.append(s)    
  
   def __str__(self):  # 리턴이 무조건 문자열을 해줘야 함.
        
        for s in self.students:
            print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)
        return "" 

 
 
