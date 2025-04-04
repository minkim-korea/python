#문서 읽어오기 -r 
#일반 파일 읽어오기 -rb 
# f= open("python/p0404/a.jpg","rb")#파일읽기
# ff = open ("C:/down/b.jpg","wb") #파일쓰기 
#이진파일은 용량이 클수있으므로 ,1byte읽어오기
# while True:
#     fData = f.read(1)
#     if not fData:break 
#     #len = ffwrite(fData)
# f.close()
# print("파일 읽어오기 완료")

# fData = f.read(1)  
# f.close()
# print("파일 읽어오기 완료 ")
# #문서저장 -w ,a
# #파일저장 -wb 
# #폴더 존재 확인: os.path.exists()
# #폴더생성 :  os.makedir() 폴더1개생성 - c:/down1/aaa/a.jpg 
# #폴더 생성 : os.makedirs() 모든폴더생성 -c:/down1/aaa/a.jpg
# import os 
# #폴더가 없으면 생성후 진행 
# if not os.path.exists("c:down1"):
#     os.makedirs("c:/down1")
# ff= open("C:/down/b.jpg","wb")
# len = ff.write(fData)
# print(f"파일크기 : {len} 바이트 ")
# ff.close()
# print("파일 저장완료")