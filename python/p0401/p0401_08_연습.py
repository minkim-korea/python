#퀴즈 singer = {}
##각각의 가수가 몇번 존재하는 출력하시오 
#"지드래곤 ": 6
list =["지드래곤","황가람","제니","리쿠","에스파",
       "지드래곤","지드래곤","지드래곤","황가람","황가람","황가람",
       "지드래곤","지드래곤","지드래곤","황가람","황가람","황가람",
       "제니","리쿠","에스파","제니","리쿠","에스파","제니","리쿠","에스파",
       "제니","리쿠","에스파","제니","리쿠","에스파","제니","리쿠","에스파"]

singer = {}
for i in list : 
   if i not in singer:
     singer[i]=1 
   else:
    singer[i]+=1
    
for i,v in singer.items(): #(key,value) 
#  =for i,v in singer.enumerate(singer):
  print(f"{i} : {v}")