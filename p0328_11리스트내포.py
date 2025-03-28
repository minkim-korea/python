# arr = [1,2,3,4,5,6,7,8,9,10]
# # arr2 = [1,2,3,4,5,.......100]
# arr2= [i+1 for i in range(100)]  # 리스트 내포 

# print(arr2)

# a_list = [1,2,3]
# aa_list = ["1m","2m","3m"]
# aaa_list=[str(i)+"m" for i in a_list]
# print(aaa_list)

# #arr2 리스트에 cm 붙여보기 
# arr2_list = [str(i)+"cm" for i in arr2]
# print(arr2_list)

# arr3_list = []
# for i in arr2 :
#     arr3_list.append(str(i)+"cm")
#     print(arr3_list)

arr = [i for i in range(100)]
# print(arr)

#리스트 내포 100개 리스트 값에 + 100을 전부 해서 출력하시오 .
arr2=[i+100  for i in arr]
print(arr2)

#위에껄 for 문으로 

a_list=[]
for i in range(100):
    a_list.append(i)
print(a_list)

aa_list = [i for i in range(100)] # 0~99 i i 
print(aa_list)