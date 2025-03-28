#1-100까지 랜덤숫자 생성 10번시도후 정답을 맞추는 프로그램을 구현하시오 .
# 도전회수 : 5
# 도전번호 : []
# 랜덤번호 : 

import random
num = []
ran_num = random.randint(1,100)
n = 0

for n in range(1,6):
    in_num = int(input("숫자를입력하세요"))
    num.append(in_num)
  
    if ran_num == in_num:
        print("정답입니다. {}".format(ran_num))
        break
    elif ran_num>in_num:
         print("{} 보다 큰수를 입력하세요".format(in_num))
    else:
         print("{} 보다 작은값입력하세요".format(in_num))
    
print("도전회수:{}".format(n))
print("입력된 숫자 :{}".format(num))
print("랜덤숫자: {}".format(ran_num))







