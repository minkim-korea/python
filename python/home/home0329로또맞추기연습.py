#로또맞추기 랜덤으로 6개 수를 받아서 출력
#-------------------형태-------------
#입력받은 숫자 6개를 my_list 에 저장을 시키는 프로그램을 구현 
#랜덤번호 : 
#입력번호 : 
#당첨개수 :
#당첨번호 :

import random
my_list = [] #저장받을 배열
ran_list = random.sample(range(1,46),6) # 랜덤번호 
lotto_c = 0 #당첨개수
lotto_n = [] # 당첨번호 
i= 0
while i < 6:
     print("랜덤번호 {}".format(ran_list))
     my= int(input("{}번째 랜덤숫자를입력하세요(1~45):".format(i+1)))
     if my not in my_list:
          my_list.append(my)
          i+=1

for j in range(6):
    #print("확인:",ran_list[j]) 정답이뭔지 확인 하려고 만듬 
    if ran_list[j] in my_list:
         lotto_c = lotto_c +1
         lotto_n.append(my_list[j])

# ran_list.sort()      숫자정렬해봄 
# my_list.sort()


print("-"*30)   #보기편하게 ----- 
print("랜덤번호는{}".format(ran_list))
print("입력번호는{}".format(my_list))
print("당첨개수는{}".format(lotto_c))
print("당첨된번호는{}".format(lotto_n))
            



