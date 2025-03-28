# a = 100
# b = 50 

# b = 100, a=50 값을 교체 
#어떻게 값을 변경하면 될까? 
#두 변수 값을 교체하려면, 추가적인 변수 c를 하나두고 값을 보관해서 교체 

# c = a
# a = b
# b = c 

# print(a)
# print(b)

# a,b = b,a #파이썬만되는 특징 a,b의 변수값 교체방법 
# print(a)
# print(b)

#입력 : input 
#출력 : print

# print(input("숫자를 입력하세요."))

# #변수() 있으면 함수 -어떠한 기능구현을 말함. 
# print()

#입력
# *****타입변경 - 정수 : int() ,실수: float() ,문자열: str()
a = input("1.숫자를 입력하세요.")
b = input("2.숫자를 입력하세요.")
a = float (a)
b = float(b)
print(a,b)
print(type(a))
print(type(b))
print(a+b) 



