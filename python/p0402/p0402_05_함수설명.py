def cal (*a,b=10):  # 가변 매개변수,키워드 매개변수함께사용시-매개변수에 키워드를 같이 넣어서준다 
    result = b 
    for i in a: 
        result += i     
    return result 

print(cal(1,2,b=100)) # b=100 이런식으로  
    
    




# #키워드 매개변수 -키워드변수는 무조건 마지막에 있어야함 . 

# def cal(a,b=10):
#     return a+b

# print(cal(1))


# #print()함수는 매개변수가 가변매개변수임 .
# print(1,2,3,4,5)
# print(1,2)





# #가변매개변수 사용
# def cal (*num): #전개 연산자 1,2,3,4,5 몇개가들어오든상관없음
#     result =0
#     for n in num:
#         result +=n
#     return result

# print("2개합계 :",cal(1,2))
# print("3개합계:",cal(10,20,30))
# print("4개합계",cal(20,40,60,80))




# def cal (n1,n2):
#     return n1+n2
# def cal2(n1,n2,n3):
#     return n1+n2+n3
# n1 =10 
# n2 =20
# n3 = 30 
# n4 = 40
# result= cal(n1,n2)
# print(result)

# result2=cal2(n1,n2,n3)
# print(result2)


# #global 변수 : 전역변수 
# def func1():
#     global a 
#     a=20 # 지역변수 이기에 함수를 벗어나면 사라짐 .
 
# a=10
# print("a:",a)#a:10
# func1() 
# print("a:",a) #a:10





# s={"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,'avg':100.0,"rank":1}
# #일반변수를 매개변수로 전달 매개변수로 일반변수 전달형태 -리턴을 값을 돌려줘서 입력을 시켜야 함. 
# #국어점수변경 함수선언
# def cal(s):

#    s['kor'] =int(input("수정할 국어점수를 입력하세요 >>>    "))
#    s['total'] =s['kor']+s['eng']+s["math"]
#    s['avg'] = s['total']/3
# print("[학생성적수정]")
# kor = 100
# eng = 100
# math = 100
# s={"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,'avg':100.0,"rank":1}

# #국어점수 변경 함수 호출
# cal(s) # 변경된 국어점수
# print("수정된 국어점수는 :",s['kor'])



# def cal(a_list):
#     a_list[0]=100
#     a_list[1]=200
# a_list=[0,0]
# a_list[0]=10
# a_list[1]=20
# a_list=[10,20] # 리스트타입 변수:주소값이있다 

# print("함수호출 전 a_list : ",a_list[0],a_list[1])
# cal(a_list) #함수호출  b_list= a_list
# print("함수호출 후 a_list : ",a_list[0],a_list[1])



# #함수선언
# def cal(a,b
#         ):
#     a=100     # 지역변수 -함수내 일반변수는 함수를 벗어나면 사라짐 일반변수-bool int float str 
#     b=200
#     #------------
# #함수밖 
# a=10          #전역변수
# b=20
# print("함수호출전 a,b:",a,b)

# #함수호출
# cal(a,b)
# print("함수호출 후 a,b: ",a,b)

# students=[
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,'avg':100.0,"rank":1},
#     {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,'avg':99.67,"rank":2},
#     {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,'avg':99.67,"rank":2},
    
# ]

# def stu_print():
#    for s in students:
#     print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}")


# print("1.학생성적입력")
# print("2.학생성적출력")
# choice =int(input("원하는번호입력>>"))

# if choice==2:
#     stu_print()




#이름 ,국어 ,영어 ,수학 점수를 입력받아 , 합계를 평균을 출력하시오 

#함수선언
# def cal(kor,eng,math):
#     return kor+eng+math,(kor+eng+math)/3 

# no=1
# name = (input("이름을 입력하세요.>>"))
# kor = int(input("국어점수를 입력하세요"))
# eng = int(input("영어점수를 입력하세요"))
# math= int(input("수학점수를 입력하세요"))

# total,avg =cal(kor,eng,math)
# print("합계:",total,"평균:",avg)








# 직사각형 넓이와 둘레를 구하는 프로그램을 구현하시오 . 
# 가로 * 세로 (가로+길이)*2
# 가로 ,세로길이를 입력 받아 넓이와 둘레를 구하시오 
# def cal(n1,n2):
#  result1 = n1* n2
#  result2 = (n1+n2)*2
#  return result1,result2 

# #가로 세로 입력 
# n1 = int(input("가로길이를 입력하세요.>>"))
# n2 = int(input("세로길이를 입력하세요.>>"))
# result1,result2 =cal(n1,n2)
# print("넓이:",result1, "길이:",result2)
# cal(n1,n2)












# # 입력을 5개를 받아 , 짝수만 모두 더한 값을 출력 
# def even(n):
#     if n%2==0: 
#      return n 
#     else: 
#      return 0  
 
# def cal(n_list): 
#     sum=0
#     for n in n_list:
#         if n%2 == 0: sum += n
        
#     return sum
# n_list=[0]*5
# for i in range(5):
#     n_list[i]=int(input("숫자입력:"))
# result=cal(n_list)
# print("짝수의 합 : ", result)














# 함수사용 - 1중복코드 2.소스복잡할때
#먼저 프로그램 모두 구현해놓고 중복되 고있는 확인 후 함수를 사용 


 









#함수를 사용해서 두수를 입력받아 
# 10~ 20입력받아 10+11+.....20 출력하시오

# def add(n1,n2):
#  if n1> n2 :
#      n1,n2=n2,n1
#  sum=0 
# #프로그램 구현 
#  for i in range(n1,n2+1):
#     sum +=i
#  print("합계: ",sum)

# n1 = int(input("숫자 입력하세요.>>"))
# n2 = int(input("숫자 입력하세요.>>"))
# # 큰수를 먼저 넣어도 .10,2 ->2,10 

    
       
# add(n1,n2)

# # #add()결과 값을 출력하시오 
# # def add(n1,n2):

















#num1,num2,num3 값을 입력받아 , 합계, 평균을 구하시오 






# def add(n1,n2,n3):
#     return n1+n2+n3 
# n1= int(input("점수입력하세요.>>"))
# n2= int(input("점수입력하세요.>>"))
# n3= int(input("점수입력하세요.>>"))
# total= add(n1,n2,n3)
# avg= total/3 
# print(n1,n2,n3,total,avg)
