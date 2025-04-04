a_list = ['홍길동','홍길순','홍길자','이순신','김유신','김구','순신스']

while True:
    name = input("찾고자하는 이름 입력 >>>")
  
    temp=0 
    for a in a_list :
        # if name== a: # 똑같을때만 검색이 됨  
        if name in a : # 글자에 특정문자가 포함되어 있으면 검색 
            print(f"{name}으로 검색된 {a}을(를) 찾았습니다.") 
            temp =1 
    if temp ==0:
         print(f"{name}을 찾지못했습니다. 다시입력 >>")