# import stu_func
import stu_func as stu  #별칭사용방법 
# from   stu_func import stu_print,stu_input,stu_output #각각의 함수명 
# from stu_func import* 모든함수 다가지고와 
# import random 
from stu_func import *
import random 

# stu.txt 파일에서 데이터를 읽어와 students =[] 데이터를 입력 시키기
# 
students = []
#파일불러오기 
with open("python/p0404/stu.txt","r",encoding="utf8") as f: 
 while True:             #여러줄일때 반복문 적용 
    line = f.readline()  # 1줄읽어오기 
    if not line : break  #데이터없을때 종료 
    s = line.strip().split(",") #1줄 문자열을 .기준으로 분리 
    students.append({"no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3]),"math":int(s[4]),"total":int(s[5]),"avg":float(s[6]),"rank":int(s[7])})

   

count= 4
title= ['번호','이름','국어','영어','수학','합계','평균','등수']
choice = 0



#ctrl shift k      삭제 단축키 
#shift alt 방향키   복사 단축키 
  

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
 
 

 elif choice==5:
     students2 = [*students]    
     print("[학생성적정렬]")
     print("1.이름순차정렬")
     print("2.이름역순정렬")
     print("3 합계순차정렬")
     print("4.합계역순정렬")
     print("5.번호순차정렬")
     print("6 번호역순정렬")
     print("0.이전화면이동")
     print("-"*50)
     choice =int(input("원하는번호 선택>>>"))
     if choice ==1:
        students2.sort(key=lambda x:x['name'])
     if choice ==2:
        students2.sort(key=lambda x:x['name'],reverse=True)
     elif choice==3:
        students2.sort(key=lambda x:x['total'])
     elif choice==4:
        students2.sort(key=lambda x:x['total'],reverse=True)
     elif choice==5:
        students2.sort(key=lambda x:x['no'])
     elif choice==6:
        students2.sort(key=lambda x:x['no'],reverse=True)
     elif choice==0:
         continue 
    
        
         
           
     
     stu.stu_output(title,students2)
     
 elif choice==6:
     print("[학생성적삭제]")
     name= input("삭제하고자하는 학생이름 입력>>")       
     temp=0
     for i,s in enumerate(students):     
         if name == s['name'] :
            temp=1
            print(f"{s['no']}번 {name}학생을 찾았습니다.")
            answer = input("학생성적을 삭제할까요? y (삭제하시면 복구불가)")
            if answer == 'y':del students[i]           
            print(f"{name}학생을 삭제했습니다. ")
            print()    
            break
     if temp == 0:
       print(f"{name}학생을 찾지 못했습니다 다시입력해주세요 ")
       print()           
                       
 elif choice==7: #학생성적저장
     print("[학생성적저장]")
     with open("python/p0404/stu.txt","w",encoding="utf8") as f:
       for s in students: # 1,홍길동,100,100,100,300,100.0,1
           line = f"{s["no"]},{s["name"]},{s["kor"]},{s["eng"]},{s["math"]},{s["total"]},{s["avg"]},{s["rank"]}\n"
           f.write(line)
     print("파일이저장되었습니다.")
     print() 
 elif choice==0:
        print("[프로그램종료]")
        break
    