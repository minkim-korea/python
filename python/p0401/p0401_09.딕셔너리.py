# # myset1= {1,2,2,3,3,3,5,5,7}
# # #= set ->중복제거 키를 확인 
# # print(myset1)


# # menu_list = ["삼각김밥","바나나","사과","바나나","도시락","삼각김밥"]
# # print(set(menu_list))# list 타입을 set타입으로 변경해서 확인

# #----------------------------------------------------------------------------

# list =[ 1,2,3,4,5]
# # list2 = [101,102,103,104,105]
# list2 = [i+100 for i in list]
# print(list2)

# list =[ 1,2,3,4,5]
# #list +100*100
# # list2 = ['10,100','10,200','10,300','10,400','10,500']
# #format  함수 천단위 표시 
# list2 = ["{:,d}".format((i+100)*100) for i in list ] # 암기 
# print(list2)
#################################################################

#리스트 내포 :if 조건절을 넣을수 있음 단 한줄만! 
# n_list=[i for i in range(1,51) if i%3==0]
# print(n_list)

#2개의 리스트를 출력할수있음. 
# n_list= ["홍","유","이",'강',"김"]
# t_list= [100,99,89,89,100]

# for n,t in zip(n_list,t_list):
#     print(f"{n}:{t}")
     
# dic = {}
# students = {"no":1,"name":"홍길동","kor":100}
# for key,value in students.items():
#     print(f"{key}:{value}")


 #zip( ->2개 리스트를 합치는것 -> list타입변경 dict타입변경 가능 )
n_list= ["홍","유","이",'강',"김"]
t_list= [100,99,89,89,100]
         
print(list(zip(n_list,t_list))) #list 수정 불가능
print(dict(zip(n_list,t_list))) #dict 수정 가능
[
 ['홍',100],
 ['유',99],
 
 
 
 ]

# tuple_list= list(zip(n_list,t_list))
