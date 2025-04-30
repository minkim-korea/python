import dbconn
                       
print("------------------db연결--------------------------")
# db접속 
conn =dbconn.connections() # sql dev 프로그램오픈 
cursor = conn.cursor() # sql창 오픈
## employees 에 salary 4000~ 6000사이의 사번 ,이름 월급을 출력하시오 

name =input("검색하려는 이름을 입력하세요.>>")

#query ="select employee_id,emp_name,salary from employees where salary between 4000 and 6000 "
name = '%'+name+'%'
query ="select employee_id,emp_name,salary from employees where emp_name like :name "
cursor.execute(query,name=name) # sql구문넣어서 실행  f9 누른거임 

rows = cursor.fetchall() #데이터를 가져옴.

for r in rows:
    print(r[0],r[1],r[2])  #튜플형태로 들어옴 리스트처럼 사용
    
    
