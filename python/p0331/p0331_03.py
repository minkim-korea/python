# # # # #for
# # # # for i in range(10):
# # # #     print(i)
# # # #     #10번반복 
# # # # #for i in range(0,1,2) 2위치는 간격설정 
# # # # #while

# # # # i=0
# # # # while i <10:
# # # #      print(i)
# # # #      i+=1

# # # #10번의 숫자를 입력받아 ,합계를 구하시오 
# # # #for 문 while 문 2가지 
# # # # i=0
# # # # sum=0
# # # # while i<10: 
# # # #  g=int(input("{}숫자를입력하세요 :".format(i+1)))
# # # #  sum=sum+g
# # # #  i=i+1
# # # # print(sum)
 
# # # # for i in range(10):
# # # #     g=int(input("{}숫자를입력해주세요".format(i+1)))
# # # #     sum+=g
# # # #     i+=1
# # # # print(sum)

# # # #로또맞추기 
# # # #6개 랜덤 숫자와 입력숫자 6개를 출력하시오.
# # # ####내가대충만든거##################
# # # # import random
# # # # a=[]
# # # # ran_a =random.sample(range(1,45+1),6)

 
# # # # for i in range(6):
# # # #     x=int(input("{}숫자를입력하세요:".format(i+1)))
# # # #     if x not in a :
# # # #      a.append(x)
# # # # print("입력번호",a)
# # # # print("로또번호",ran_a)
# # # ##########내가 대충만든거######################### 


# # # ##########     정석 ################ 
# # # # import random
# # # #lotto =[]
# # # #my_input=[]
# # # #for i in range(6):
# # #    #lotto.append(random.randint(1,45))

# # # #for i range(6):
# # # # num = int(input("숫자를 입력하세요. "))
# # # #my_input.append(num)
# # # ###########정석########################
# # # # import random
# # # # lotto = [i+1 for i in range(45)] # 1,2,3........44,45
# # # #lotto_input=[]
# # # #my_input=[]

# # # #lotto_input=random.sample(lotto,6)# 리스트에서중복없이 6개를 가져옴 
# # #    #lotto.append(random.randint(1,45)) # 중복가능 
# # # #for i in range(6):

# # # #for i range(6):
# # # # num = int(input("숫자를 입력하세요. "))
# # # #my_input.append(num)

# # # #print("로또번호",lotto_input)
# # # #print("입력번호",my_input)

# # # ######################정석###########################
# # # # import random
# # # # a_list = [i+1 for i in range(45)]
# # # # print(a_list)

# # # # random.shuffle(a_list) #shuffle 
# # # # print(a_list)
# # # # print(a_list[:6])
# # # #-------------------------------------
# # # # import random  
# # # # #random.random()함수 : 0<=x<1 사이의 랜덤실수를 가져옴.
# # # # print(random.random()) # 0.0000000<=x <1.00000000
# # # # print(random.randint(1,10)) 
# # # # print(int(random.random()*10)+1) #1부터10까지 랜덤숫자를 뽑아줌 
# # # # print(int(random.random()*10)+0) #0부터 9 까지 랜덤숫자를 뽑아줌 
# # # # print(random.randint(1,10))


# # # #반복문 for , while
# # # # a_list = [i+1 for i in range(100)]
# # # # print(a_list)

# # # # a_list 에서 홀수의 합계를 구하시오 . 
# # # # sum=0

# # # # for i in a_list:
# # # #  if i%2==1 : # 홀수이면 
# # # #   sum= sum+i  # i의 값을 합계변수에 더함. 

# # # # print("홀수합계:",sum)

# # # #1-100까지의 숫자의 합을 구할때 합계가 200을 넘을때 숫자를 출력하시오 
# # # # 1+2+3+4+......200이 넘는 위치값을 출력하시오
# # # #break
# # # sum=0
# # # i=0
# # # a_list = [i+1 for i in range(100)]
# # # for i in a_list:
# # #     sum= sum+i 
# # #     if sum>200: break
    
    
# # # print(f"i: {i}, sum:{sum}")
# # # print(f"i-1: {i-1}, sum{sum-i}")

# # #  #----------------------------------------
 
 
# # #  #입력한 숫자의합이 50을 넘으면 프로그램을 종료하고 
# # #  #총합을 구하시오 .
# # #  #입력한숫자 중 5의배수는 제외


# # # # continue, break ,pass ->실행할 구문이 없음 . for 문을 계속반복 
# # # #1-10까지 진행을 하는데 1,2,3-contiunue:제외 4,5,6,7,8,9,10
# # # # continue = 그위치에서 중지후 맨처음으로 실행 
# # # # 1-10까지 진행을 하는데 1,2,3-break 반복문 종료 
# # # # break 반복문 탈출 
# # # # 1-10까지 진행을 하는데 1,2,3-pass , 4,5,6,78,9,10 10번실행 
# # # # pass 
# # # # sum=0 
# # # # while True : 
# # # #     if sum<50:
# # # #      num= int(input("숫자입력:"))
# # # #      if num%5==0:
# # # #          print(f"{num},5의배수는 제외")
# # # #          continue # 실행을 1번 중지 #pass와 차이점이있다. 
# # # #      sum=sum+num
# # # #     else: break
    
# # # print(f"합계:{sum}")
# # # #################################################################
# # # # for i in range(10):
# # # #     if i%2 ==1 : continue #1회중지
# # # #     print(i)
    
# # # # for i in range(10):
# # # #     if i%2 ==0 : pass
# # # #     print(i)
    
# # # # for i in range(10):
# # # #     if i%2 ==0 : break
# # # #     print(i)

# # # i=0
# # # for i in range (10):
# # #     for j in range(i) :
# # #         print("*",end=" ") #end 옆쪽으로 출력해라~ 
        
# # #     print()
    
# # # a_list = [1,2,3,4,5]
# # # print(a_list[5])
# # # #error

# # # #역순 출력 :: - 
# # # a_list= [1,2,3,4,5,6,7,8,9]
# # # print(a_list[::-1])

# # # #값변경 
# # # a_list [5]= 10
# # # print(a_list)

# # # #값을 변경 할때 1:2 2의 위치값이 포함 
# # # a_list[1:2] =[100,200]
# # # print(a_list)


# # # #1차원 리스트 
# # # aa=[10,20,30]
# # # #2차원리스트
# # # aa =[[1,2,4],[5,6,7,8],[9,10,11,12]]

# # # print(aa[0])
# # # print(aa[0][0])

# # # a_list=[
# # # [1,2,3],    #[0][0], [0][1],[0][2]
# # # [4,5,6],    #[1][0], [1][1],[1][2]
# # # [7,8,9]     #[2][0], [2][1],[2][2]
# # # ]
# # # for i in range(3): # 0,1,2
# # #     for j in range(3): # 0,1,2
# # #         print(a_list[i][j],end="\t")
        
# # # print(a_list)
# # #####################################
# # # 퀴즈 
# # #1,2,3,4,5
# # #6 7 8 9 10 
# # #11 12 13 14 15
# # #16 17 18 19 20
# # #21 22 23 24 25 

# # a_list=[[1,2,3,4,5],
# #         [6,7,8,9,10],
# #         [11,12,13,14,15],
# #         [16,17,18,19,20],
# #         [21,22,23,24,25]
# #     ]

# # for i in range(5):
# #      for j in range(5):


# #         print(a_list[i][j],end="\t")
# #      print()
# #1-25
# import random
# a_list = [i+1 for i in range(25)]
# random.shuffle(a_list)
# print(a_list)
# #랜덤으로 섞여진 리스트 출력 
# print(a_list)

# import random # 1.순차적 리스트생성
# #2리스트섞기
# random.shuffle(sample_list)
# a_list= [[0]*5 for i in range(25)]
# sample_list=[i+1 for i in range(25)]
# #[12345....25]
# #a_list = [[1,2,3,4,5],.....
# # .......[21,22,23,24,25]
# a_list = [[0]*5 for i in range[5]]
# for i in range(5):
#     for j in range (5):
#         a_list[i][j]=5*i|(j+1)
# #5x5리스트 초기화
# a_list=[[0]*3]*5 # 얕은복사 
# a_list=[[0]*5 for i in range(5)] # 깊은복사 #어렵다
# print(a_list)
# for i in range(5): 
#     for j in range(5):
#            a_list[i][j]=sample_list[5*i+(j+1)]       
        
# print(a_list)

# a_list=[[0]*3]*5 # 얕은복사 
# a_list=[[0]*5 for i in range(5)] # 깊은복사 #어렵다
# print(a_list)
# for i in range(5): 
#     for j in range(5):
#            a_list[i][j]= 5*i+(j+1)        
        
# print(a_list)

# #5x5 리스트 출력 

# for i in range(5):
#      for j in range(5):
#         print(a_list[i][j],end="\t")
#      print()
    #졸아서 이상함 # 졸아서 이상함 
sample_list = [[0]*5 for i in range(5)]
#print(sample_list)
    
    
    #5 x 5fltm 0으로초기화 
sample_list = list ()
for i in range(5):
     temp =[]
     for j in range (5):
         temp.append(0) # [0,1,2,3,4]  [0,0,0,0,0]
     sample_list.append(temp)#[000000]
     print(sample_list)