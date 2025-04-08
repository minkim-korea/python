a = "홍길동님! 안녕하세요 . 반갑습니다. 안녕 반가워. 안녕안녕"
#a.find() for 문을 사용해서 안녕이 몇번나오는지 개수를 출력하시오. 
num = a.count("안녕") #count 함수 
# print(num)
# target ="안녕"
# count = 0
# i=0

# #while문사용 
# while i <=len(a) -len(target):
#     if a[i:i+len(target)]== target:
#         count+=1
#         i+=len(target)
#     else:
#         i+=1
# print(f"{target}은/는 총 {count}번등장합니다.")

# ##############################################
# # for문 사용  
# for i in range(len(a)-len(target)+1):
#      if a[i:i+len(target)]== target:
#         count+=1
# print(f"{target}은/는 총 {count}번등장합니다.")  

#글자가 있는지 확인
#if "안녕" in a :
# print("안녕이라는 글자가 있습니다.")
#글자가 있으면 위치 알려줌.
# print(a.find("안녕"))

i = 0
count=0
while True:
    num = a[i:].find("안녕")
    if num !=-1: # 못찾으면 -1 
       count+=1
       i +=num+1 
    else: break
    
print("개수:",count)

# print((a[i:].find("안녕")))
# print(a[0+6+1:].find("안녕"))
# print(a[0+6+1+13+1:].find("안녕"))
# print(a[0+6+1+13+1+7+1+1+1:].find("안녕"))