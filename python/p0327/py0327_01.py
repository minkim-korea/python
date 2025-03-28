# #파이썬 변수타입
# # bool 타입 True False 
# # 숫자 : int 타입-정수 , float 타입 -실수
# # 문자열 : str


# #변수선언 
# abc=10
# a=20
# num=30

# # #print()
# # print("안녕")
# print("안녕", a)
# # print("입력된 숫자 :{}".format(a))
# print(f"입력된숫자 : {a}")
# print("입력된 숫자: %d" %(a))
# print("입력된 숫자: {}".format(a))

# #입력 input 타입 :str 타입 
# #입력된 값은 타입 str타입이기 때무넹 형변환을 해줘야 함.
# num1=float(input("숫자를 입력하세요.>>"))
# num2=float(input("숫자를 입력하세요.>>"))
# print("입력된숫자는 : {:.0f},{:.0f} / 합계 : {:.0f}".format(num1,num2,num1+num2))

#학생성적 프로그램 
#이름, 국어 ,영어 , 수학 , 입력받아서, 합계,평균을 출력하는 프로그램을 구현 
# /print("-"*50)
# print("학생성적프로그램")
# print("-"*50)
# name = input("이름을 입력하세요 :")
# kor = int(input("국어점수를 입력하세요 :"))
# eng =int( input("영어점수를 입력하세요 :"))
# math =int( input("수학점수를 입력하세요 :"))
# total= kor+eng+math
# avg= total /3
# print()
# print("이름\t국어\t영어\t수학\t합계\t평균")
# print("-"*50)
# print("{}\t{}\t{}\t{}\t{}\t{:.1f}".format(name,kor,eng,math,total,avg))







