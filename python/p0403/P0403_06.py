# import stu_func
import stu_func as stu  #별칭사용방법  
# from   stu_func import stu_print,stu_input,stu_output #각각의 함수명 
# from stu_func import* 모든함수 다가지고와 
# import random 
students = []      
count= 1
title= ['번호','이름','국어','영어','수학','합계','평균','등수']
choice = 0

  

while True:
 #화면출력부분 
 choice = stu.stu_print()
   #학생성적입력부분 
 sub_list= ["",'kor','eng','math'] 

 
 if choice ==1 :
   count = stu.stu_input(count,students)
        
 elif choice==2:
    stu.stu_output(title,students)
 elif choice==3:
        print("[학생성적 수정]")
        name= input("수정하려고하는 학생이름을 입력하세요>>")
        temp = 0 # 찾지못했을경우 
        for s in students:
            if s["name"] == name: 
                temp = 1
                print(f"{name}학생을 찾았습니다. 과목을 수정합니다")
                print("[수정과목 선택]")
                print("1.국어")
                print("2.영어")
                print("3.수학")
                print("-"*30)
                choice =int(input("원하는번호를 입력하세요"))
                if choice ==1:
                    pre_score = s[sub_list[choice]]
                    print(f"현재 {title[choice+1]}: {pre_score}")
                    s[sub_list[choice]] = int(input(f"수정할 {title[choice+1]} 점수입력:"))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total'] /3
                    print(f"변경전{pre_score}을 {s[sub_list[choice]]}으로 변경되었습니다.")
                elif choice==2:
                    pre_score = s[sub_list[choice]]
                    print(f"현재{title[choice+1]}점수:{pre_score}")
                    s[sub_list[choice]] = int(input(f"수정할 {title[choice+1]}점수입력:"))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total'] /3
                    print(f"변경전{pre_score}을 {s[sub_list[choice]]}으로 변경되었습니다.")
                elif choice==3:
                    pre_score = s[sub_list[choice]]
                    print(f"현재{title[choice+1]}점수:{pre_score}")
                    s[sub_list[choice]] = int(input(f"수정할 {title[choice+1]}점수입력:"))
                    s['total'] = s['kor']+s['eng']+s['math']
                    s['avg'] = s['total'] /3
                    print(f"변경전{pre_score}을 {s[sub_list[choice]]}으로 변경되었습니다.")
        if temp ==0:
            print(f"{name} 학생은 존재하지 않습니다. 다시입력하세요!! ")
            print()
            
        
        
        
 elif choice== 4: #등수처리 
     stu.stu_rank(students)
          
 elif choice==0:
        print("[프로그램종료]")
        break
    