### board 테이블, bfile 테이블
### bfile 테이블:   a1.jpg     a2.jpg 저장하기 
##3 bno : 시퀀스번호 


from stuconn import *
## 1. db연결
conn = connections()

## 2, 게시글작성ㄴ 
btitle = "파일첨부 게시글 제목입니다."
bcontent ="파일첨부 게시글 내용입니다."
query = " insert into  board values(:bno,:btitle,:bcontent,'aaa',:bno,\
    0,0,0,sysdate)"


##2. 시퀀스번호 생성 : bno에 저장
cursor=conn.cursor()
cursor.execute("select board_seq.nextval from dual") 
bno = cursor.fetchone()[0] # 모양이 튜플 (입력된숫자다음숫자,0)

## 3-1 db에 게시글 저장 
cursor.execute(query,bno=bno,btitle=btitle,bcontent=bcontent)
conn.commit()



## 3. 리스트형태로 파일생성  - a1.jpg,a2.jpg
## 이런형태로 만들예정[[bno,a1.jpg],[bno,a2.jpg]]
bfilelist = []
bfilelist.append([bno,'b1.jpg'])
bfilelist.append([bno,'b2.jpg'])

## 4. db에 파일저장 
query ="insert into bfile values(:1,:2)"
cursor.executemany(query,bfilelist)
conn.commit()
##5. 프로그램 종료 
conn.close()
print("프로그램종료")