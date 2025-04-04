#파일 읽어오기 
# 1 . open()  2. f.read() 3. f.close()
# r: 읽기 w: 쓰기 a: 이어쓰기
f = open("python/p0404/stu.txt","r",encoding="utf-8")
# 여러줄이니까 반복문 진행 
students=[]
while True:
    data = f.readline()
    if not data : break
    #1,홍길동,60,100,100,260,86.66666666666667,3\n
    #strip():공백제거 split(): 분리 
    s = data.strip().split(",")
    students.append({
                     "no":int(s[0]),"name":(s[1]),"kor":int(s[2]),"eng":int(s[3]),
                     "math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7])})

f.close()
print(students)


# [{'no': 1, 'name': '홍길동', 'kor': 60, 'eng': 100, 'math': 100, 'total': 260, 'avg': 86.66666666666667, 'rank': 3}, {'no':
# 2, 'name': '유관순', 'kor': 100, 'eng': 80, 'math': 99, 'total': 279, 'avg': 93.0, 'rank': 1}, {'no': 3, 'name': '이순신', 'kor': 100, 'eng': 100, 'math': 55, 'total': 255, 'avg': 85.0, 'rank': 4}, {'no': 4, 'name': '강감찬', 'kor': 80, 'eng': 60, 'math': 71, 'total': 211, 'avg': 70.33333333333333, 'rank': 5}, {'no': 5, 'name': '김구', 'kor': 90, 'eng': 90, 'math': 98, 'total': 278, 'avg': 92.66666666666667, 'rank': 2}]