class Car: 
    speed = 0
    tire = 4
    door = 5 
    def speeUp(self,s):
        self.speed += s 
        print("현재속도 : ",self.speed)
        
class Sedan(Car):
    color = "red"
c =Car()
# print(c.geartype) #없는 변수 출력시 에러 

s = Sedan()
print(s.tire)