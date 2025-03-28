# # 반복문 while - 조건식이 맞으면 무한 반복 가능 
# i = 0 
# while i<10:
#     print(i) 
#     i +=1 #1씩증가
    
#     print("-"*50)
    
#     #반복문 for -횟수만큼 반복 
#     for j in range(10):
#       print(j)
# i=0    
# while True:
#     print(i)
#     i+=1
    
# input_list = [1,5,10,9,8,20]
# a = 5 
# if a in input_list: # input_list안에 a가 있는지 확인하는형태 
#     print("{}가 존재합니다.".format(a))
# else:
#     print("{}존재 ㄴㄴ".format(a))

# #입력한 숫자를 5번 반복해서 리스트에 추가하는프로그램 구현 
# num_list = []

# for i in range(10):
#      num = int (input("숫자  입력 :"))
     
        
     
#      num_list.append(num)

# print(num_list)
#-----------------------------------------------
# num_list = []

# for i in range(10):
#      num = int (input("숫자  입력 :"))
#      # num가 num_list가 있는 지 확인해서 없으면 입력 있으면제외
#      if num not in num_list:
#          num_list.append(num)
        
     
     
# print(num_list)
num_list = []
i=0
while i<10:
    num = int (input("{}번째숫자를 입력 :".format(i+1)))
    if num not in num_list:
         num_list.append(num)
         i+=1
        
print(num_list)