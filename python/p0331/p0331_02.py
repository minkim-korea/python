# #삭제 del, pop,remove,clear
# a_list=[1,2,3,4,5]
# del a_list[2]# 위치값삭제
# print(a_list)

# a_list.pop() #맨뒤 삭제,특정위치 삭제가능 
# print(a_list)

# a_list.remove(1) # 데이터값으로 삭제 
# print(a_list)


# a_list.clear() # 전체삭제
# print(a_list)


#
# #리스트 - append를 활용해서 추가하는방법 
# a_list =[]
# # for i in range(1,11):
# #     a_list.append(i)    
# # print(a_list)
# # #리스트 내포 append랑 똑같음 이게더빠름
# # a_list = [i for i in range(1,11)]
# # print(a_list)

# list추가: #append,insert,extend 추가하는방법들 
# a_list=[1,2,3]
# a_list.append(4)  # 마지막에 추가 
# print(a_list)
# a_list.insert(1,100) # 특정위치에 값을 추가해라
# print(a_list)
# a_list.extend([100,200,300])
# print(a_list)


# # #index 번호를 넣으려면 enumerate를 사용한다.중요 
# a_list=[273,10,5,9,100,1000,50]
# for idx,value in enumerate(a_list):
#     print(f"{idx+1}: {value}")
    