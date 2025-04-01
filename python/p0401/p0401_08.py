list = [1,2,3,1,2,3,5,6,8,9,10,1,2]
dic ={}

for i in list :
    print(i)
   # dic 에 추가 , dic 키존재 확인 
    if i not in dic:
        dic[i]= " "
    # dic[i] = dic[i] +1  # 키가 몇개존재하는지 개수를 파악 
    dic[i] +="■"
for i,d in enumerate(dic):
    print(f"{i} : {dic[d]}")
        
print(dic)

#-------------------------------------------------------


#dic ={1:3,2:3,3:1,5:1,6:1,8:1,9:1,10:1}

