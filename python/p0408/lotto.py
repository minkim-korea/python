#lotto 프로그램 
import random
my_lotto=[]
ran_lotto = random.sample(range(1,45),6)
l_count =0 
l_num =[]
i=0
while i < 6:
    my = int(input("랜덤으로 숫자를입력하세요(1-45) :"))
    if my not in my_lotto:
        my_lotto.append(my)
        i+=1

for  j in range(6):
    if ran_lotto[j] in my_lotto:
        l_count+=1
        l_num.append(ran_lotto[j])
        
print("랜덤번호는{}".format(ran_lotto))
print("입력번호는{}".format(my_lotto))
print("당첨개수는{}".format(l_count))
print("당첨된번호는{}".format(l_num))
            