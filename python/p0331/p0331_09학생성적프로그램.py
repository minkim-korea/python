#초기화선언
students =list()
count= 1
#프로그램시작
while True:
 print("-"*40)
 print(""*10,end="")
 print("[학생성적 프로그램]")
 print("-"*40)
 print("1. 학생성적입력 ")
 print("2. 학생성적출력")
 print("3. 학생성적수정")
 print("4. 학생성적삭제")
 print("5. 학생성적정렬")
 print("6. 학생성적검색")
 print("0. 프로그램종료")
 print("-"*30)
 no = count
 name = input("이름을 입력하세요 >>")
 kor  = int(input("국어점수를 입력하세요>>"))
 eng  = int(input("영어점수를 입력하세요>>"))
 math = int(input("수학점수를 입력하세요>>"))
 total= kor+eng+math
 avg = total/3
 rank = 0

 student = [no,name,kor,eng,math,total,avg,rank]
 students.append(student)
 count+=1

    
#번호입력
 choice = int (input("원하는 번호를 입력하세요.>>"))
 print()
 #원하는 프로그램 실행    
    
 if choice== 1:
     print("[학생성적 입력]")
 elif choice==2:
    print("[학생성적출력]")      
        
 elif choice ==0:
     print("[프로그램 종료]")
     break
     print()        
print()