# 학생성적 프로그램 
# 이름, 국어 ,영어 , 수학 , 입력받아서, 합계,평균을 출력하는 프로그램을 구현 
print("-"*50)
print("                 학생성적프로그램")
print("-"*50)
name = input("이름을 입력하세요 :")
kor = int(input("국어점수를 입력하세요 :"))
eng =int( input("영어점수를 입력하세요 :"))
math =int( input("수학점수를 입력하세요 :"))
total= kor+eng+math
avg= total /3
print()
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(name,kor,eng,math,total,avg))

