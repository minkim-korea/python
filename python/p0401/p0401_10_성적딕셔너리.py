students=[
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,'avg':100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,'avg':99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,'avg':99.67,"rank":2},
    
    
        #  [1,'홍길동',100,100,100,300,100.0,1],
        #  [2,'유관순',100,100, 99,299,99.67,2],
        #  [3,'이순신',100,100,99,299,99.67,2] 
]
#print(students)
count = 4 # 학생번호를생성
title= ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    print(" "*25,end="")
    print("     [학생성적프로그램]")
    print("-"*50)
    print("1, 학생성적입력")
    print("2. 학생성적출력")
    print("-"*50)
    choice= int(input("번호입력 ㄱㄱ>>"))  
#입력번호 확인 
  
    if choice == 1:
     while True :
       print("[학생성적입력]")
       no=count
       name= input(f"{no}학생이름입력 ㄱㄱ(0.이전화면이동))>>")
       if name == '0' :break
       kor = int(input("국어점수입력 ㄱㄱ>>"))
       eng = int(input("영어점수입력 ㄱㄱ>>"))
       math = int(input("수학점수입력 ㄱㄱ>>"))
       total = kor+eng+math
       avg= total/3 #  나누기 ->float 타입
       rank= 0
       students.append(
            {"no":no,"name":name,"kor":kor ,"eng":eng,"math":math,
                "total":total,"avg":avg,"rank":rank})  
       print(f"{name}학생성적이 입력되었습니다.")
       print()
       count+=1 #학생번호 1증가 
       
       
       # for문
    #   score = [0]*3 # kor eng math 넣을예정
    #   for i in range (3):
    #       score[i] =int(input(f"{title[i+2]}점수를입력하세요.>>"))
           
    elif choice==2:
        print(""*20,end="")
        print("[학생성적출력]")
        print("-"*30)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
        print("-"*30)
        for s in  students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s["total"]}\t{s["avg"]}\t{s["rank"]}")
                  
    elif choice==0:
      print(":[프로그램종료]")
      print()
      break