# if 10>3:
#     print("정상")
# else:
#     print("비정상")

# # print(int("안녕1")) 에러 숫자형태문자열만 숫자타입으로변경가능 

# print(int(1.5)) # 실수형-> 정수형으로 타입변경 " 소수점이 사라짐 /

# # print(int("1.5")) 문자열 flat 타입을 int 타입으로 변경안됨 
# # print(float("1.5"))
# # print(str(1.5))

# # list_a = [1,2,3,4] # 매우중요 
# # print(list_a)
# # print(list_a[0]+list_a[1]+list_a[2]+list_a[3])

# # #input() 데이터 입력받음
# # score = input("데이터를입력해주세요>>")
# # print("입력데이터 : ", score)

# # ##두수를 입력받아 합계 평균을 출력하시오 
# n=input("숫자를입력하세요:")
# n2=input("숫자를입력하세요:")
# print(n+n2) # 100200
# #문자열 타입-> int타입으로 변경 
# n=int(input("숫자를입력하세요:"))
# n2=int(input("숫자를입력하세요:"))
# print(n+n2) # 300

# #조건문
# score = int(input("점수를 입력하세요 >>"))

# if score>=60:
#     print("합격")
# else:
#     print("불합격")

# score = int (input("점수를 입력하세요"))
# if score>=70:
#     print("합격")
# elif score>=60:
#     print("재시험")
# else : 
# print("불합격")
    
    #90점이상 ABCDF 출력하시오 
    
score = int(input("점수를입력하세요"))
    
if score>=90: print("A")
elif score>=80: print("B")
elif score>=70: print("C")
elif score>=60: print("D")
else :print("F") 