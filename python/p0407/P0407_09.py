class Stu:
    def __init__(self,no,name,kor,eng):
        self.__no=no
        self.__name=name
        self.__kor=kor #__언더바2개 private 접근 제한: 캡슐화
        self.__eng=eng
    def getNo(self):return self.__no
    def getName(self):
        return self.__name
    ###############################
    # @어노테이션@property,  @변수 .setter - getter,setter 만들어짐 
    # @property   # print(s.kor)
    
    # def kor(self):
    #     return self.__kor
    # @kor.setter  # s.kor = 90  s.kor =150 # raise에러 
    # def kor (self,kor):
    #    if kor >=0 and kor<=100:           
    #         self.__kor=kor
    #    else:       
    #         raise NotADirectoryError("유효한 값이 아닙니다.")
    ##############################
    def getkor(self):
        return self.__kor
     #setter
    def Setkor(self,kor):
        if kor >=0 and kor<=100:           
            self.__kor=kor
        else:       
            raise NotADirectoryError("유효한 값이 아닙니다.")
    #getter
    def getEng(self):
        return self.__eng
    #setter
    def setEng(self,eng):
        if eng>=0 and eng<=100:
            self.__eng=eng
        else:raise NotImplementedError("유효한 데이터가 아닙니다.")
    def __str__(self):
        return f"{self.no},{self.name},{self. __kor},{self.eng}"
s=Stu(1,"홍길동",100,99)
s.__kor=200  #s.kor
print(s.no,s.name,s.__kor) #지역 변수 개념의 s.__kor의 값 출력
s.eng=300
s.Setkor(500)
print(s)