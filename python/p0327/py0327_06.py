# # 
# num =  7
# if 10>=num>=0:
#     print("10에 해당되는 숫자입니다.")
    
# if 10>=num and num>=0:    
# print("10에 해당되는 숫자입니다.")
# 숫자를입력받아 봄여름 가을 겨울을 출력하시오 . 
# 345-> 봄의 계절입니다.
# 678-> 여름의 계절입니다.
#91011->가을의 계절입니다.
#1212-> 겨울의 계절입니다.

season= int(input("월을 입력해주세요:"))
if 3<=season<=5:
    print("봄의 계절입니다.")
elif 6<=season<=8:
    print("여름의 계절입니다.")
elif 9<=season<=11:    
    print("가을의 계절입니다.")
else:
    print("겨울의 계절입니다.")
    if season==1 :
        print("")
    elif season==12:
        print("")
    elif season==2:
         print("")
    else :
        print("omg 그것은 달이아닙니다")
    