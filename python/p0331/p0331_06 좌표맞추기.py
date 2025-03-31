# x 좌표 : 1 
# y 좌표 : 3 
# -> x ,y 좌표 1,3 으로 동시에입력 시키기 

num1 = int (input("x좌표: "))
num2 = int (input("y좌표: "))

print(f"[x,y좌표: {num1},{num2}]")

num= input ("x,y좌표(0,0): ")
n_list = num.split(",")  # split , 를기준으로 분리 시켜줌 

print(f"[x,y좌표: {n_list} ]")
