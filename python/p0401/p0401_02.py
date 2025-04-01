a_list = [1,2,3,4,5]
#"X""X""X"]
count = 0
while True:
    #g화면출력
 print(a_list)
#숫자입력
 num= int(input("숫자를입력:"))
 for i in range(len(a_list)): # len(a_list) = 5 
    if a_list[i] ==num:
        a_list[i] = "X"
        count +=1
        break

    
    #x개수확인
 if count >= 5 :
     print("빙고완성!!")   
     print(f"완성개수:{count}")
     break
 
 print(f"현재 X개수:{count}")