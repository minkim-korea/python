a_list =[ ["X","X","X","X","X"],[6,"X",8,9,10]]


no=0
for i in range(5):
    if a_list[0][i] == "X":
        no+=1
if no ==5:
    print("빙고완성!!")
    
print(f"현재 [0]방의 x개수 : {no}")
