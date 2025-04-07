class Student:
    # #인스턴스 변수 -객체선언시 각각 변수들이 존재 :공용으로 사용안됨 . 
    # no   = 1
    # name = "" #인스턴스 변수 
     count = 1    #클래스변수 -모든 객체가 공용으로 사용하는 변수 
     kor   = 0
     eng   = 0
     math  = 0
     total = 0
     avg   = 0.0
     rank  = 0
     def __init__(self,name,kor,eng,math):
      self.no=Student.count  #인스턴스 변수 
      self.name=name
      self.kor=kor
      self.eng=eng
      self.math=math
      self.total=kor + eng + math
      self.avg = self.total/3
      self.rank = 0
      Student.count += 1            #1증가

a=[1,2,3,4,5]

s= Student("홍길동",100,100,99)
print(s)
print(a)

def __str__(self) :
    return f"""{self.no},{self.name},{self.kor},{self.eng},{self.math}, {self.total} ,{self.avg:.2f} ,{self.rank}"""
s = Student("홍길동",100,.100,99)
print(s)




# #매개변수가 있는 생성자를 활용해서 데이터 입력 
# s= Student("홍길동",100,100,99) # 매개변수가 있는 생성자 객체선언 
# print(s.no,s.name,s.kor,s.eng,s.math,Student.count-1)
# s2 =Student("유관순",99,99,98)
# print(s2.no,s2.name,s2.kor,s2.eng,s2.math,Student.count-1)
# s3 =Student("이순신",90,90,91)
# print(s3.no,s3.name,s3.kor,s3.eng,s3.math,Student.count-1)






# a_list = [1,2]
# 기본생성자를 가지고 객체선언후 데이터 입력 
# s = Student() # 기본생성자 
# s.name ="홍길동"
# print(s.no, s.name)

# s2 = Student() 
# s2.no = 2
# s2.name = "이순신"
# print(s2.no, s2.name)