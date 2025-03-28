#로또 번호 자동생성 프로그램 
import random

#반복을 해서 ran_list 10개를 입력시키는 프로그램 단 중복 숫자 제외
# ran_list = []
# i=0
# while i<6:
#     ran_input= random.randint(1,45)

#     if ran_input not in ran_list:
#          ran_list.append(ran_input)
#          i+=1
        
# print(ran_list)


#랜덤 1-45 번까지 숫자 6개 ran_list 저장 
#입력받은 숫자 6개를 my_list 에 저장을 시키는 프로그램을 구현 
#랜덤번호 : 
#입력번호 : 
#당첨개수 :
#당첨번호 :
ran_list = random.sample(range(1,45+1),6)
my_list = []
lotto_count= 0
lotto_list=[]
i= 0
while i<6:
     print("랜덤번호: {}".format(ran_list))
     my_input= int(input("{}번째숫자를입력하세요".format(i+1)))
     if my_input not in my_list:
        my_list.append(my_input)
        i+=1
 
 #당첨비교 프로그램
 
# for j in range(6):
#     for k in range(6):
#       if ran_list[j]==my_list[k]:
#          lotto_count = lottoo_count +1
#          lotto_list.append(my_list[k])
#          break            


for j in range(6):
    print("확인:",ran_list[j])
    if ran_list[j] in my_list:
         lotto_count = lotto_count +1
         lotto_list.append(my_list[j])
            
   
print("랜덤번호: {}".format(ran_list))
print("입력번호: {}".format(my_list))
print("당첨개수: {}".format(lotto_count))
print("당첨번호: {}".format(lotto_list))
