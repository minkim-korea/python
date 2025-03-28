# #for문 중복 하기 
# # 두수를 입력받아 두수 사이의 합게를 구하시오 . 
# # 예시 1 이랑 7 1234567까지 합을 출력하면된다

# num1 = int(input("숫자입력해라 "))
# num2 = int(input("숫자입력해라"))
# sum= 0
# i = 0 

# for i in range(num1,num2+1) :
#     sum= sum + i

# print("{}에서 {}까지의합계 :{}".format(num1,num2,sum))

# # # if 문 비교 num1 num2 
# num1 = int(input("숫자입력해라 "))
# num2 = int(input("숫자입력해라"))
# sum= 0
# i = 0 
#  if num1>num2 :
#   t= num1
#   num1=num2
#   num2=t
 
#  num1,num2=num2,num1#파이썬만 가능 
    

# # for i in range(num1,num2+1) :
# #     sum= sum + i

# # print("{}에서 {}까지의합계 :{}".format(num1,num2,sum))

#구구단 출력 for 문 2번 돌려야됨 
# for i in range(2,9+1):
#     if i%2==1:
        
#       print("[{}단]".format(i))
#       for j in range(1,9+1):
     
#         print("{}x{}={}".format(i,j,i*j),end=" ")
#     print()
    
    
#시작단과 끝나는 단을 입력받아 , 출력하시오 
# 2 ,6 2~6단까지 출력 

# num1=int(input("시작단을입력하시오"))
# num2=int(input("끝단을 입력하시오"))
# i=0
# for i in range (num1,num2+1):
#     print("[{}단]".format(i))
#     for j in range(1,9+1):
        
#         print("{}x{}={}".format(i,j,i*j))
#     print() 
    
num1=int(input("시작단을입력하시오"))
num2=int(input("끝단을 입력하시오"))

if num1>num2:
   num1,num2=num2,num1
 # num1,num2=num2,num1#파이썬만 가능
# t = num1
# num1=num2
# num2=t 
 
for i in range (num1,num2+1):
    print("[{}단]".format(i))
    for j in range(1,9+1):
        
        print("{}x{}={}".format(i,j,i*j))
    print() 