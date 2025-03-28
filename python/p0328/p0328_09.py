# for i in range(1,1000):
#     print("{:03d}".format(i))
    
    
    #구구단을 출력하시오 
    # 2 x 1 = 2 
    
for i in range(1,10):
    #print("[ {}단 ]".format(i))
    for j in range(2,10):
        print("{} x {} = {}".format(j,i,i*j),end="   ")
        