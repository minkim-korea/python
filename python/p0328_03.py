# # 반복문을 사용해서 1-10까지 출력 

# # for i in range(1,11) :
# #   print(i)
  
# # a = 10
# # if a>5 and a<9: 
# #   print(a) 
      
# # if a>5 or a<9: 
# #   print(a) 

# a_list = [1,2,3,4,5]
# print(a_list[2])
# print(a_list[1:4]) # [시작위치 :끝나는위치-1]-슬랑이싱 
# print(a_list[:3]) #  [:끝나는위치-1]-처음부터 시작해라
# print(a_list[2:]) # [시작위치:] 끝까지 출력 
# print(a_list[::2]) # 2개씩 증가해서 출력 
# print(a_list[::3]) # 3개씩 증가해서 출력 
# print(a_list[::-1]) # 역순출력 ㄷㄷ
# print(a_list[:-1])
# a ="안녕하세요"
# print(a[2])
# print(a[1:4])
# print(a[:3])
# print(a[2:])
# print(a[::3])
# print(a[::-1])
# print(a[:-1])

# print(a[:7])# 슬라이싱은 없는 값 출력 시 에러가 나지않음 
# #print(a[7]) 인덱싱 없는것 출력시 에러 인덱스에러 

# print(len(a_list))#리스트 개수확인
# print(a_list[:len(a_list)-1])
# print(len(a)) # 문자열길이

# a_list[1:11:2]
# for i in range(1,11,2):
#   print(i,end=" ") # 줄바꿈없이 출력 end=""
  
  
# sum = 0 
# for i in range(1,100+1):
#   sum= sum+i
  
# print("1-100까지합계 : {}".format (sum))


#합계가 100  넘는 위치의 숫자는 얼마일까요 ? 
  
sum = 0 
i = 0
for i in range(1,100+1):
  sum= sum+i
  print("i:{}, sum: {} ".format(i,sum))
  if sum>=100:break
  
  
print("1-100까지합계 : {}".format (sum))
print("i:{}",i)
print("sum:",sum)
