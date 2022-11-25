'''변수(variable)
어떤 데이터를 저장하고자 할 때 사용하는 메모리 저장소.'''

'''변수명 작성 규칙
  영문, 한글, 숫자 밑줄(_)로 구성된다. (단, 한글은 최대한 절대 쓰지 말 것)
  특수문자(!@#$%^&*()_+등)은 사용할 수 없다..
  대문자와 소문자를 구분한다.
  변수명의 첫 글자를 숫자로 사용할 수 없다.
  키워드 (list, dict, if, for, and 등)은 사용할 수 없다.'''


name = 'Alice'
print(name)
age = 25
print(age)
address = '''우편번호 12345 
서울시 영등포구 여의도동 1234-5
'''
print(address)

'''잘못된 변수명 예시
숫자로 시작하면 안됨
하이픈 안되고 언더바만 가능
공백있으면 안 됨
'''

# 2mybar = 'Python1'
# my-var = 'Python2'
# my var = 'Python3'

#주석 단축키는 Ctrl + / (끄는 것도 똑같음)
#줄 복사(줄의 내용을 똑같이 복사) 단축키는 Ctrl + D

'''여러 값 할당 
 Python을 사용하면 한 줄에 여러 변수에 값을 할당할 수 있다
 '''

x, y, z = "피카츄", "라이츄", "파이리"
print(x) #피카츄
print(y) #라이츄
print(z) #파이리
print(x,y,z) #피카츄 라이츄 파이리

'''
여러 변수에 대한 하나의 값
 한 줄에 여러 변수에 동일한 값을 할당할 수 있다.
 '''
x = y = z = '꼬부기'
print(x) #꼬부기
print(y) #꼬부기
print(z) #꼬부기
