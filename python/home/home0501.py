from dbconn import *  

conn=connections() # 오라클접속 
cursor =conn.cursor() # sql developer 연결 

while True:
    print(" [학생성적프로그램]")
    print("1.학생성적입력")
    print("2.학생성적출력")
    print("-"*30)
    choice=int(input("원하는번호를 입력하세요>>>"))
    
    if choice ==1:
        ### 직접입력 
        name =input ("이름을 입력하세요.>>")
        kor = int(input ("국어점수를 입력하세요.>> "))
        eng = int(input ("영어점수를 입력하세요.>> "))
        math = int(input ("수학점수를 입력하세요.>> "))
        total = kor+eng+math
        avg = total/3
        ####insert 1개저장
        query= "insert into stuscore values(\
        stuscore_seq.nextval,:name,:kor,:eng,:math,:total,:avg,0)"
        cursor.execute(query,name=name,kor=kor,eng=eng,math=math,total=total,avg=avg)
        conn.commit()
        print(name,'학생성적이 저장되었습니다.')
        print()

    elif choice==2:
        pass
    else:
        break

#종료
conn.close()
print("[프로그램 종료]")








# ###select 한개데이터가져오기
# query = 'select count(*) from stuscore'
# cursor.execute(query)
# cnt =cursor.fetchone() # 실행 결과 - 한개 
# print("학생수:",cnt[0])  #(100,)
# #cnt =cursor.fetchall() # 실행 결과 - 한개 
# #print("학생수:",cnt[0][0]) #[(100,)] 



# ###select- 여러개 데이터 가져오기 
# query='select * from stuscore'
# cursor.execute(query) #명령문 실행 
# rows = cursor.fetchall()   # 실행 결과 -여러개 
# for r in rows:
#     print(r)
     


