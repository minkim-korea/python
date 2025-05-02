# 오라클 db연결
import oracledb as ora 

## 오라클 접속 -외부연결 : 에러가났을때 예외처리를 해주는게좋음

def connections():
    try: conn= ora.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
    except Exception as e: print(e) 
    return conn 
    
        