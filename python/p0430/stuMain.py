### 학생성적 프로그램 
###진행 
students=[]
title=['번호','이름','국어','영어','수학','합계','평균','등수']

count = 1

while True:
    print("-"*40)
    print("           [학생성적프로그램]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 성적순 정렬")
    print("5  삭제")
    print("6  검색")
    print("0 프로그램종료")
    print("-"*40)
    choice = int (input("번호를 입력하세요"))
     
   

    if choice==1:
        while True:
            print("[학생성적 입력]")
            no=count
            name=input(f"{no}번 학생 이름을입력하세요.(0.이전화면 이동)>>")
        
            if name == "0" :
                break
            while True:
                kor = input("국어점수를입력하세요.>>")
                if kor.isdigit():
                    kor =int(kor)   
                    if 0<= kor <=100: 
                      break 
                    else: print("점수는 0-100사이의값을 입력하셔야합니다.")    
                else: print("숫자만 가능합니다.")
            
            while True:   
                eng = input("영어점수를입력하세요.>>")
                if eng.isdigit():
                    eng =int(eng) 
                    if 0<= eng <=100:
                      break 
                    else: print("점수는 0-100사이의값을 입력하셔야합니다.")    
                else: print("숫자만 가능합니다.")
            
            while True:    
                math = input("수학점수를입력하세요.>>")
                if math.isdigit():
                    math =int(math)   
                    if 0<= math <=100: 
                      break 
                    else: print("점수는 0-100사이의값을 입력하셔야합니다.")    
                      
            total = kor + eng +math
            avg = total/3
            rank = 0
            print(f"{no}번 {name}학생 성적을 저장했습니다.")
            students.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,'avg':avg,"rank":rank})
            print()
            count += 1
    
    elif choice == 2 :
        print("학생성적 출력")
        print("-"*50)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*50)
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
                
    elif choice ==3: 
         print("-"*50)
         print("학생성적 수정")
         name = input("수정하려고 하는 학생이름을 입력하세요.(0.이전화면이동)>>")
         temp = 0 
         for s in students:
           if name in s['name'] :
               temp =1
               print(f"{name}학생이 있습니다. 성적을 수정합니다. ")
               print("1.국어") 
               print("2.영어") 
               print("3.수학") 
               choice = int(input("원하는 번호를 입력하세요"))
               if choice ==1 :
                   pre_kor=s['kor']
                   print(f"현재국어점수 {pre_kor}")
                   s['kor']=int(input("변경 국어점수:"))
                   s["total"] = s['kor']+s["eng"]+s["math"]
                   s["avg"] = s["total"]/3
                   print(f"국어점수{pre_kor}점을 {s['kor']}으로 변경되었습니다.")
               if choice ==2 :
                   pre_eng=s['eng']
                   print(f"현재영어점수 {pre_eng}")
                   s['eng']=int(input("변경 영어점수:"))
                   s["total"] = s['kor']+s["eng"]+s["math"]
                   s["avg"] = s["total"]/3
                   print(f"영어점수{pre_eng}점을 {s['eng']}으로 변경되었습니다.")
               if choice ==3 :
                   pre_math=s['math']
                   print(f"현재수학점수 {pre_math}")
                   s['math']=int(input("변경 수학점수:"))
                   s["total"] = s['kor']+s["eng"]+s["math"]
                   s["avg"] = s["total"]/3
                   print(f"수학점수{pre_math}점을 {s['math']}으로 변경되었습니다.")
               
    elif choice ==4:
        students.sort(key=lambda x:x["total"],reverse=True)
        print("정렬완료")
       
               
    elif choice ==5:
          name= input("삭제할 학생이름")
          for s in students:
              if s['name'] ==name:
                  students.remove(s)       
                  print("삭제완료")
                  break
       
               
    elif choice ==6:
        name = input ("검색할 학생이름")
        for s in students:
            if s['name']==name:
        
              print(f"{name}을/를 찾았습니다.")
              break 
            else : 
              print(f"{name}을/를 못찾았습니다.")  
             
    elif choice ==0:
        print("프로그램종료합니다")
        break
         
         
            
            