#이름, 국어,영어,수학 입력받아 합계,평균을 출력하시오 
#합계 : 300
#이름 : 홍길동
# 평균 : 100.0 소수점은 1자리까지 출력하시오 

# a=input("이름을 입력하세요 :" )
# b=input("국어점수를 입력하세요 ")
# c=input("영어점수를 입력하세요 ")
# d=input("수학점수를 입력하세요 ")
# b=float(b)
# c=float(c)
# d=float(d)
# print(b,"+",c,"+",d,"=",b+c+d)
# total= b+c+d
# print("total: %.1f" % (total/3))

# name= input ("이름입력")
# kor = int(input("국어점수입력"))
# sci = int(input("과학점수입력"))
# eng = int(input("영어점수입력"))
# math= int(input("수학점수입력"))
# total= kor+eng+math
# avg=(kor+eng+math)/3

# print("이름 : ",name)
# print("국어 : ",kor)
# print("영어 : ",eng)
# print("수학 :",math)
# print("합계 : ", kor+eng+math)
# print("평균:%.1f" % avg)
 
 #프린트시 \n 엔터키 , \t : tab키 
 #format()문자형태 지정 
# print("안녕하세요.\n 반갑습니다.\t 저는 홍길동이라고합니다.")
a=10
b=3
print("%d / %d = %.2f" %(a,b,a/b))
str_print="{} / {} = {:.2f}".format(a,b,a/b)
str_print2=f"{a}/{b}={(a/b):.2f}"

print(str_print2)

