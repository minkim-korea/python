#1차원 리스트 
# s_list=[i for i in range(1,26)]
# s_list=[i for i in range(25)]
#print(s_list)

import random
s_list=[i for i in range(1,26)] #1차원리스트생성
random.shuffle(s_list) 
# random.random(), random.randint() random.sample() random.shuffle()
print(s_list)   

# 2차원 리스트
# my_list = [[0]*5 for _ in range(5)] # 2차원리스트생성
# print(my_list)

# my_list[0][1] =1 #값변경
# print(my_list)

#1차원리스트값 -> 2차원리스트 입력
my_list = [[0]*5 for _ in range(5)] # 2차원리스트생성

for i in range(5):
    for j in range(5):
      my_list[i][j] = s_list[5*i+j] # 5x+y 5x+0
      

        #화면출력
while True:
 print(""*5,end="")
 print("    [좌표맞추기프로그램]")
 print("-"*50) 
 print("*  |",end="\t")
 for i in range(5):
   print(i,end="\t")
 print()
 print("-"*50)
      
 for i in range(5):
    print(f"{i} |",end="\t")
    for j in range(5):
         print(my_list[i][j],end="\t")
    print()
   
   
 print("-"*45) 
 #좌표입력 x 표시 
#  x= int(input("x좌표를입력하세요>>"))
#  y= int(input("y좌표를입력하세요>>"))

#  my_list[y][x] = "X" 
  
#번호입력 x표시
#25개 모두표시 

 num = int(input("1-25까지 번호를 입력하세요.>>"))
 stop=0
 for i in range(5):
    for j in range(5):
        if my_list[i][j]== num :
         my_list[i][j]= "X"
        break     
    if stop ==1: break
    
    

    
    
    
    