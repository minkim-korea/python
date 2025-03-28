# # for 문이지요 
# # 숫자맞추기 프로그램 만들기 ! 
# import random
# #randint(1.45) 1~45사이 숫자1개를 무작위로 가져옴 
# input_list =[]
# lotto = random.randint(1,45)


# #-------
# for i in range(10):
#     input_num = int(input("{} 숫자 입력gktpdy(1~45사이) >".format(i+1)))
#     input_list.append(input_num) # 리스트에 숫자추가 
#     #랜덤번호와 입력번호를 비교 
#     if lotto==input_num:
#         print("당첨")
#         break # for문 종료 
#     elif lotto>input_num:
#         print("땡~ {}보다더큰수입력하세요".format(input_num))
#     else:
#         print("땡~ {}보다작지롱~".format(input_num))
# #-------
# print("랜덤번호 : {}".format(lotto))
# print("입력번호 : {}".format(input_list))


