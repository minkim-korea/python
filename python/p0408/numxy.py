#숫자맞추기 
import random 
f_list =[i+1 for i in range(25)]
random.shuffle(f_list)
a_list = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        a_list [i][j] = f_list[5*i+j]
        
    
while True:
    print("숫자맞추기")
  
    print()
    for i in range(5):
        print(f"{i}|",end="\t")
        for j in range(5):
            
          print(a_list[i][j],end="\t")
        print()
    num = int(input("1-25 숫자를 입력하세요(입력하신숫자는 하트로변해요):"))
    
    for i in range (5):
      for j in range(5):
         if a_list[i][j] ==num:a_list[i][j]= "♡"
    print()
 
