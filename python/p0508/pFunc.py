import oracledb

# db연결
def connections():
    try: conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    except Exception as e: print(e)
    return conn
# 1.전체 출력 
def stuAllSelect(sql='select * from stuscore2'):
       conn = connections()
       cursor = conn.cursor()
       cursor.execute(sql)
       rows = cursor.fetchall()
       for r in rows:
            print(r)
       cursor.close()
       conn.close()
       
# 2.학반별 최고등수 출력 
def stumaxtotal():
    conn = connections()
    cursor = conn.cursor()
    sql = "select sno,total,sclass from stuscore a where  total in (select max(total) maxtotal from stuscore b where a.sclass =b.sclass group by sclass)"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for r in rows:
            print(r)
    conn.commit()
    cursor.close()
    conn.close()

# 3.학반별 최하등수 출력 
def stumintotal():
    conn = connections()
    cursor = conn.cursor()
    sql = "select sno,total,sclass from stuscore a where  total in (select min(total) mintotal from stuscore b where a.sclass =b.sclass group by sclass)"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for r in rows:
            print(r)
    conn.commit()
    conn.commit()
    cursor.close()
    conn.close()
#4 부서별 최고연봉 출력 
def maxsalary():
    conn = connections()
    cursor = conn.cursor()
    sql = "select * from employees where (department_id,salary) in(select department_id,max(salary) from employees group by department_id)"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    conn.commit()
    cursor.close()
    conn.close()



#6.회원정보 rownum을 사용 , 11-20번출력 
def sturownum():
    conn = connections()
    cursor = conn.cursor()
    sql = "select * from (select rownum rnum,a.*from(select *from member order by id) a)b where rnum between 11 and 20"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    conn.commit()
    cursor.close()
    conn.close()