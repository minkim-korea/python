# 5*5 2차원 리스트 -> 랜덤으로 1-25까지 숫자를 넣기
#1차원 리스트 생성
#1차원 리스트를 랜덤으로 섞기
#2차원 리스트를 생성
#2차원리스트에 1차원 랜덤 번호를 넣기 
import random
# 1차원리스트생성후 랜덤 섞기 
first_list=[i+1 for i in range(25)]
random.shuffle(first_list)
#2차원 리스트 생성후 1차원 리스트 값을 넣기 
a_list=[[0]*5 for i in range(5)] 
for i in range(5):
    for j in range(5):
        a_list [i][j]= first_list[5*i+j]# 0-24
# print(a_list)
while True:
#2차원 형태로 출력
 print("           [좌표맞추기 프로그램]")
 print("-"*50)
 print("*  |",end="\t")
 for i in range(5):
    print(i,end="\t")
 print()
 print("-"*40)
 for i in range(5):
    print(f"{i} |",end="\t")
    for j in range(5):
        
        print(a_list[i][j],end="\t")
    print()
    #입력부분
 print("-"*45)
 num1 = int(input("x좌표:"))    
 if num1 <0 or num1>4 :
     print("숫자를 잘못입력하셨습니다.다시입력해라")
     continue
     
 num2 = int(input("y좌표:"))
 if num2<0 or num2>4 :
     print("숫자를 잘못입력하셨습니다.다시입력해라")
     continue

#좌표에 값넣기 
 a_list[num2][num1] = "X"
 print()












import random
# 1차원리스트생성후 랜덤 섞기 
first_list=[i+1 for i in range(25)]
random.shuffle(first_list)
#2차원 리스트 생성후 1차원 리스트 값을 넣기 
a_list=[[0]*5 for i in range(5)] 
for i in range(5):
    for j in range(5):
        a_list [i][j]= first_list[5*i+j]# 0-24
# print(a_list)
while True:
#2차원 형태로 출력
 print("           [좌표맞추기 프로그램]")
 print("-"*50)
 print("*  |",end="\t")
 for i in range(5):
    print(i,end="\t")
 print()
 print("-"*40)
 for i in range(5):
    print(f"{i} |",end="\t")
    for j in range(5):
        
        print(a_list[i][j],end="\t")
    print()
    #입력부분
 print("-"*45)

num = 15 
#  num1 = int(input("x좌표:"))    
#  num2 = int(input("y좌표:"))
            
#  if num1 <0 or num1>4 :
#      print("숫자를 잘못입력하셨습니다.다시입력해라")
#      continue
     
#  if num2<0 or num2>4 :
#      print("숫자를 잘못입력하셨습니다.다시입력해라")
#      continue
#좌표에 값넣기 
a_list[num2][num1] = "X"
print()