#집에서 연습해보기 
# 랜덤숫자 

import random
n = []
n = 0 

ran_random = random.randint(1,100)
in_random = int(input("숫자를입력하세요:"))

for n in range(1,10):
      .append(in_random)
    if ran_random==in_random :
        print("정답입니다 {}".format(ran_random))
    elif ran_random>in_random:
        print("{}보다작은값을입력하세요".format(in_random))
    else :
        print("{}보다큰값을입력하세요".format(in_random))
        

    