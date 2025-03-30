#집에서 연습해보기 
# 랜덤숫자 

import random
num = []

ran_num= random.randint(1,100)
n =0 

for n in range(1,6):
    in_num = int(input("숫자를입력하세요:"))
    num.append(in_num)
    if ran_num==in_num :
        print("정답입니다. {}".format(ran_num))
        break
    elif ran_num>in_num:
        print("{}보다 큰값을입력하세요".format(in_num))
    else :
        print("{}보다작은값을입력하세요".format(in_num))
        
print("도전회수:{}".format(n))
print("입력숫자:{}".format(num))
print("랜덤숫자{}.".format(ran_num))

    