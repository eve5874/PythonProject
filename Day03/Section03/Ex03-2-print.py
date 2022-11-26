'''
print() 함수
   sep : 출력할 value의 구분 문자
   end : value출력 후 출력할 문자 (기본값 '\n')
   file : 출력방향지정
'''

print("재미있는", "파이썬") #재미있는 파이썬
print("Python", "Java", "C", sep=",") #Python,Java,C ( sep""는 디폴트가 한칸 띄는 것)

print("안녕", end='\n')  #end=''의미는 end='\n'이라서
print("하세요") #안녕하세요

fos = open('sample.py', mode='wt')
print('print("Hello World")', file=fos)
fos.close() #sample.py라는 폴더 #wt는 write text이고 text쓰겠다는 것임.
