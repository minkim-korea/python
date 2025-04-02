students=[]
count=1
title= ['번호','이름','국어','영어','수학','합계','평균','등수']

while True :
    print(" "*25,end="")
    print("     [학생성적프로그램]")
    print("-"*50)
    print("1, 학생성적입력")
    print("2. 학생성적출력")
    print("-"*50)
    choice= int(input("원하는 번호를 입력하세요(0번은종료)>>"))
    
    if choice==1:
     while True:
        print("학생성적입력")
        no=count
        name =input("{}번에들어갈학생이름을입력하세요>>".format(no))
        if name =="0" :break
        
        kor   =  int(input("국어점수입력하세요>>"))
        eng   =  int(input("영어점수입력하세요>>"))
        math  =  int(input("수학점수입력하세요>>"))
        total = kor+eng+math
        avg   = total/3
        rank = 0
        students.append(  {"no":no,"name":name,"kor":kor ,"eng":eng,"math":math,
                "total":total,"avg":avg,"rank":rank})
        print(f"{name}학생성적이 입력되었습니다.")
        print()
        count+=1
    elif choice==2:
     break