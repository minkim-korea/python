
# with 파일 
# #with 쓰면 fclose 안써도됨 
# with open("python/p0404/a1.txt","w",encoding="utf-8") as f:
#     f.write("안녕")
# print("저장완료")


#학생성적 -> 파일쓰기 
# f = open("python/p0404/stu.txt","a",encoding="utf-8")
# count = 1
# while True:
#     no    = count 
#     name  = input("이름입력 하세요 >>(0.종료)")
#     if name=="0":break
#     kor   = int(input("국어점수입력 하세요"))
#     eng   = int(input("영어점수입력 하세요"))
#     total = kor+eng
#     lines = f"{no},{name},{kor},{eng},{total}\n"
#     f.write(lines)
#     count+=1
# f.close()
# print("학생성적이 저장되었습니다.")