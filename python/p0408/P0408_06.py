from sModule import Student


s1 = Student("홍길동",50,50,99)
s2 = Student("유관순",100,100,99)

print(s1) #class객체에서 무슨함수?? __str__

if s1 >= s2 : 
    print("합계점수가크거나같습니다.")
else: 
    print("합계점수가 작습니다.") 
