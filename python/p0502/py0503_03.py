from dbconn import *
conn = connections() 
cursor = conn.cursor()
while True:
    print("[ 학생성적프로그램 ]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적검색")
    print("5. 학생성적정렬 -이름순차정렬")
    print("0. 프로그램종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    if choice == 1:
        name = input("이름을 입력하세요.>> ")
        kor = int(input("국어점수를 입력하세요.>> "))
        eng = int(input("영어점수를 입력하세요.>> "))
        math = int(input("수학점수를 입력하세요.>> "))
        total = kor+eng+math
        avg = total/3
        query = "insert into stuscore values(\
        stuscore_seq.nextval,:name1,:kor1,:eng1,:math1,:total1,:avg1,0)"
        cursor.execute(query,name1=name,kor1=kor,eng1=eng,math1=math,total1=total,avg1=avg)
        conn.commit()
        print(name,"학생 성적이 저장되었습니다.")
        print()