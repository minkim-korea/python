#카드 SPADE-4 ,DIAMOND-3 ,HEART-2, CLOVER-1 
#번호 1-A,2,3,4,5,6,7,8,9,10,11-J,12-Q,13-K
#카드 1장 - 카드모양, 번호 
#카드모양 4개 
#번호는 13개 
#카드 총 개수: 52장 카드가 존재

#리스트 -딕셔너리 형태로 
clist =[
{"shape":"SAPDE",'no':1}, 
{"shape":"SAPDE",'no':2} 

]
cList=[]
# sh=[ "CLOVER","HEART","DIAMOND","SPADE" ]
sh=[ "♣","♥","◆","♠" ]
no=["","A",'2','3','4','5','6','7','8','9','10','J',"Q",'K']
import random
#카드생성
for i in range(52):
    
 cList.append({"shape":i//13,"no":i%13+1})
 #카드랜덤섞기
random.shuffle(cList)
 #myCard ,youCard
 # 5장입력
myCard = []
youCard = []

#카드5장씩 배분
for i in range(5):
   myCard.append(cList[i])
for i in range(5,10):
    
   youCard.append(cList[i])
 #내카드출력 
print("[내카드]")
for i in myCard:
     print(f"[{sh[i['shape']]},{no[i['no']]}]")
 #상대 카드 출력 
print("[상대카드]")
for i in youCard:
      print(f"[{sh[i['shape']]},{no[i['no']]}]")





score = [0]*5

for i in range(5):
    if myCard[i]['no']>youCard[i]['no']:
         score[i]=2
    elif myCard[i] ['no']< youCard[i]['no']:
         score[i]=1
    else:
        score[i] = 0 
print("[카드 승부 확인]")
print(f"승리{score.count(2)},패배{score.count(1)},무승부{score.count(0)}")
print(f"[승리카드]")
for i,c in enumerate(myCard):
 if score[i]==2:
     print(f'[{sh[c['shape']]},{no[c['no']]}]',end=" ")







# score = {"mywin":0,"youwin":0,"draw":0}

# for i in range(5):
#     if myCard[i]['no']>youCard[i]['no']:
#          score['mywin'] +=1
#     elif myCard[i] ['no']< youCard[i]['no']:
#          score['youwin']+=1
#     else:
#         score['draw'] +=1
# print("[카드 승부 확인 ]")
# print(f"승리{score['mywin']},패배{score['youwin']},무승부{score['draw']}")

  
 #승리한 카드 출력 

 #패배 카드 출력 
 
 #무승부 카드 출력  
 
    
      
      
# 11-J 12-Q 13-K 1-A
#전체 카드출력 
#
# for c in cList:
#     print(c['shape'],c['no'])








# import math
# import random 
# # 0.00000000000000 <= x <1.00000000000000
# print(random.random())
# #1-45까지 숫자 중 1개를 랜덤으로 추출 
# print(random.randint(1,45))

# #리스트에서 1개 랜덤추출 
# a_list = [1,2,3,4,5]    
# print(random.choice(a_list))
# #리스트 에서 개수만큼 랜덤추출 -중복없이 

# print(random.sample(a_list,5))

# #리스트를 랜덤으로섞기-리스트 순서를 랜덤으로 섞기 
# random.shuffle(a_list)
# print(a_list)
           
# a = 3.141592
# b = 3.51582


# a에서 소수점 3자리에서 올림해서 2자리까지 표시해서 출력하시오  # 3.15

# #a * 100 / 100 
# a*100 # 314.1592 
# print(math.ceil(a*100) /100) # 3.15 

# b에서 소수점 5자리에서 ceil올림해서 4자리까지 표시해서 출력
# print(math.ceil(b*10000) /10000)

# math안에 있는 함수를 보는방법
# print(dir(math))







# #올림 
# print(math.ceil(a)) # 4

# #반올림
# print(round(a)) # 3
# print(round(b)) # 4
# print(round(b,3)) # 소수점3자리까지 표시 ->3.516
# print(round(a,4)) # 소수점4자리까지 표시 ->3.1416

# #버림
# print(math.floor(a)) # 3
# print(math.floor(b)) # 3

