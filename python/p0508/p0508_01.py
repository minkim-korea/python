from pFunc import *

while True:
    print("[학생성적 프로그램]")
    print("1.학생전체출력")
    print("2.학반별 최고등수 출력")
    print("3.학반별 최하등수 출력")
    print("4.부서별 최고연봉 출력")
    print("5.stuscore2 학반 부여(1-10,1...)")
    print("6.회원정보 rownum을 사용 ,11번-20번 출력")
    print('-'*20)
    choice = input ("원하는 번호를 입력하세요 .>>")
   
    if   choice == "1":
        stuAllSelect()
    elif choice == "2":
         stumaxtotal()
    elif choice == "3":
         stumintotal()
    elif choice == "4":
         maxsalary()
    elif choice == "5":
         break
    elif choice == "6":
         sturownum()
    