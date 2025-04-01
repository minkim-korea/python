# 좌표 맞추기 프로그램 구현하시오 
import random
f_list = [i+1 for i in range(100)]
random.shuffle(f_list)
a_list=[[0]*10 for i in range(10)] 

for i in range(10):
    for j in range(10):
        a_list [i][j]= f_list[10*i+j]

while True:
    
 print("           [좌표맞추기 프로그램]")
 print("-"*50)
 print("*  |",end="\t")
 for i in range(10):
    print(i,end="\t")
 print()
 print("-"*40)
 
 for i in range(10):
    print(f"{i} |",end="\t")
    for j in range(10):
        
        print(a_list[i][j],end="\t")
    print()
    
 print("-"*45)
 num = int(input("1-100번 숫자를 입력하세요>>"))
 
 for i in range (10):
     for j in range(10):
         if a_list[i][j] ==num:a_list[i][j]= "X"
 print()
