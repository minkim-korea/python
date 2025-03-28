import random
#0보다 같거나 크고 1미만 수를 랜덤하게 전달해줌
# 0 <= x <1
# print(random.randint(1,10))

#랜덤숫자를 맞추는 프로그램 

# ran_num= random.randint(1,5)
# in_num= int(input("랜덤숫자 맞추기!! 1-5까지 숫자1개를 입력하세요"))

# if ran_num==in_num:
#     print("정답입니다. 랜덤숫자 :{}".format(ran_num))
# else:
#     print("오답입니다.")
#     #print("오답입니다. 랜덤숫자 :{}, 입력숫자 : {}" .format(ran_num,in_num))

#1-100까지 숫자 10개를 입력받음 
num = []
#반복문
# for n in range (1,11):  
#    print(n)        
#랜덤숫자 1개 생성 
ran_num = random.randint(1,100)
n = 0 #몇번 시도 
for n in range(1,11): 
    in_num = int(input("숫자를 입력하세요 >>"))
    num.append(in_num)   #num list 타입에 데이터를 추가
   
    if ran_num == in_num:
        print("정답 {}".format(ran_num))
        break
    elif ran_num>in_num:
        print("더 큰수를 입력해라 {}".format(in_num))
    else:
        print("더 작은수를 입력해라 {}".format(in_num))
        
print("도전회수:{}".format(n))
print("입력된 숫자 :{}".format(num))
print("랜덤숫자: {}".format(ran_num))





   
       
        
        
         
        

