#파일입출력순서 파일열기- 파일읽기 ,파일쓰기 -파일닫기 
# #파일열기 -3가지모드 : r 읽기모드 w 쓰기모드  a 추가모드  b = 이진파일-파일복사 
# f= open("a.txt","r")#읽기모드
# f= open("a.txt","w")#쓰기모드
# f= open("a.txt","a")#추가모드 
#news.txt파일 출력하기 
f= open("C:/workspace/python-1/python/p0404/news.txt","r",encoding="utf-8")
for line in f:
    print(line.strip())
f.close() 

 
 #파일읽어오기 - 절대경로 사용
# f = open("C:/workspace/python-1/a.txt","r",encoding="utf-8")
f = open("python/p0404/b.txt","r",encoding="utf-8") 
#------------------------------------
# for
# for line in f:
#     print(line.strip())
# f.close()  
# while 
while True:#3줄
    line = f.readline()
    if not line :
        break
    print(line.strip())
#----------------------------------------- 
 
 
 
 
 
# 파일읽기 - readlines() : 모두 읽어 오기 
# f = open ("a.txt","r",encoding="utf-8")
# lines = f.readlines() # 모두읽어오기 
# for line in lines:
#     print(line.strip())
# f.close()








# # 파일읽기 - r  1줄 읽기 read()
# f= open("a.txt","r",encoding="utf-8")
# print(type(f))
#모든줄을 실행 for 문을 사용 
# for line in f:
#     print(line.strip())
# print("완료되었습니다.")
# f.close()