# # def add(a,b):
# #     return a+b
# # print(add(10,20))
    
    
# # def func(a,b,c):
# #     return max(a,b,c)
# # print(max(10,5,20))
# # #람다식 lambda -> 함수형태를 축약형
# # 람다식 사용방법: lambda 매개변수 : 리턴값 
# # #def 함수명(매개변수) : return 값
# # def func2(a):
# #     return a*20

# #람다식 
# # ambda a: a*20 
# def func(x):
#     return x**2

#  map함수관련
# a_list=[1,2,3,4,5] # list모든값에 제곱을 해서 리스트를 생성 
# aa_list=[]
# for i in a_list:
#    aa_list.append(i**2)    



# # map(함수,리스트) 
# print(list(map(func,a_list)))

# # 람다식 - map() 함수를 lambda로 사용하면 코드를 줄일수있다. 
# print(list(map(lambda x:x**2,a_list)))
#map()함수 : 리스트에 함수를 적용해서 다시 리스트로 반환 



# #filter ()함수: 리스트에 함수를 적용해서 조건에 맞는 것만 다시 리스트로 반환 
# a_list =[1,2,3,4,5]
# aa_list = []
# for i in a_list:
#     if i%2 == 0:
#         aa_list.append(i)
# print(aa_list)

# #filter ()함수사용
# def func(x) :
#     if x%2 == 0:
#         return x 
# b_list = list(filter(func,a_list))
# print(b_list)

# c_list= list(filter(lambda x:x%2==0,a_list))
# print(c_list)

students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
]
#sort( )기존의 리스트의 값을 변경시킴. 
#sorte 기존의 리스트는 유지 새로운 리스트 생성 
s_list = sorted(students,key=lambda x: x['name'])
print(s_list)
print("-"*60)
print(students)





# #합계정렬방법
# print(students)
# print("-"*60)
# students.sort(key=lambda x:x['total'])#합계 순차정렬 
# print(students)
# students.sort(key=lambda x:x['total'],reverse=True)#합계 역순정렬 
# print(students)



#이름을 정렬방법
# students.sort(key=lambda x :x['name']) #이름으로 순차정렬 
# print(students)
# students.sort(key=lambda x :x['name'],reverse=True) #이름으로 역순정렬 
# print(students)

# students.sort()
# print(students)  #dict타입은 sort()함수를 사용할수없음.


#리스트 sort()정렬됨.
# a_list = [20,50,10,40,90]
# a_list.sort() #순차정렬
# print(a_list)
# a_list.sort(reverse=True) #역순
# print(a_list)
