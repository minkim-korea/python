title= ['번호','이름','국어','영어','수학','합계','평균','등수']
score = [0]*3
print(score)

score[0] = 100
print(score)

score = [0]*3 # kor eng math 넣을예정
for i in range (3):
  score[i] =int(input(f"{title[i+2]}점수를입력하세요.>>"))
print(score)