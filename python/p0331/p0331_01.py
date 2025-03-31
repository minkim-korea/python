# #구구단 만들기 
# for i in range(2,10) :
#     print("[{}단]".format(i))
#     for j in range(1,10):
#         # 모양새 2 x 1 = 2 
#         print("{} x {} = {}".format(i,j,i*j))
        
#     print()   #공백 
    
# #list

# a_list = [1,2,3,4,5]
# sum = 0 
# for i in a_list:
#     sum = sum +i
    
#     print(sum)

# # print(sum)위치에따른 변화    
    
# a_list = [1,2,3,4,5]
# sum = 0 
# for i in a_list:
#     sum = sum +i
    
# print(sum)

a=10
a_list=[1,2,3,4,5]
print("a:",a)
a_list[0]= 100

print("a_list :", a_list) #[100,2,3,4,5]

#a변수와 b변수는 다른 변수임 . 
b= a
b = 1000
print("a:",a)
print("b",b)

#a_list, b_list다른리스트 인가? 
b_list=a_list

b_list[1]= 200  
print(a_list)  #주소값을 공유해서 a값도 바뀜 (얕은복사)
### 새롭게 복사 : 깊은복사하는방법은 ? 
 # *를 넣어주면됨  매우중요 
a_list=[1,2,3,4,5]
b_list=[*a_list]  
b_list[1]= 200  
print(a_list)    
print(b_list)
