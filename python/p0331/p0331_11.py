import random
f_list=[i +1 for i in range(25)]
random.shuffle(f_list)
a_list=[[0]*5 for i in range(5)]

for i in range(5):
    for j in range(5):
        a_list[i][j]=f_list[5*i+j]
        
        
while True:
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
         print(a_list[i][j],end="\t")
    print()
     
 print("-"*50)    
 num = int(input("1-25번 숫자를 입력하세요>>"))
 
 for i in range (5):
     for j in range(5):
         if a_list[i][j] ==num:a_list[i][j]= "WIN"
 print()
