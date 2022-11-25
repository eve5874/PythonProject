'''
문자열(String)
    하나 이상 연속된 문자(characther)들의 나열.
    파이썬에서 문자열 자료형은 큰따옴표("")
    또는 작은 따옴표('') 사이에 위치.
'''
#'Hello'와 "Hello"는 동일
print('Hello' == "Hello") #True
# = 표시는 대입 연산자 이고. == 표시는 비교연산자로, 같으면 True, 틀리면 False라고 뜸.

'''
변수에 문자열 할당
'''
a = "Hello"
print(a)

'''
여러줄 문자열 
   세개의 따옴표를 사용하여 변수에 여러 줄 문자열 할당
'''
a = """피카츄,라이츄,파이리,꼬부기
버터플, 야도란, 피존투, 또가스
"""
print(a)

'''
문자열 배열(배열은 값이 여러개 들어있는 것임. Hello라고 하면 실제로 문제 하나하나가 메모리 공간안에 있는 것임. H,e,l,l,o가 다 별도 공간. 
          근데 우리는 이를 다 묶어서 Hello라고 받은 것임)
   
    문자열 인덱싱(indexing)
    H    e   l    l   o <== 문자열
    0    1   2    3   4 <== 인덱스
   -5   -4  -3   -2  -1 <==마이너스 인덱스
    str 타입은 인덱스 번호를 가지고 있음. 
    '''

a = "Hello"
print(a[1]) #e
#a전체를 가져오려면 print(a) 인데, a 중에서 하나의 값(또는 특정구간의 값)만 가져오려면 인덱스 사용.
#대괄호[]가 인덱스임. 문자열의 문자값을 가져오는 것
print(a[-5]) #H
print(a[1] == a[-4]) #True

'''
문자열 슬라이싱
     슬라이스 구문을 사용하여 문자 범위를 반환할 수 있다.
     문자열의 일부를 반환하려면 시작 인덱스와 끝 인덱스를 콜론으로 구분하여 지정한다.    
     1) [2:5]이면 2번째부터 5번 직전까지를 출력하는 것)
        (공백도 문자로 인식함)
     2) [:5]이면 맨 처음부터 5번 직전까지 슬라이스
     3) [2:]이면 2번부터 끝까지 슬라이스
'''

b = "Hello, World"
print(b[2:5]) #llo
print(b[2:6]) #llo,
print(b[2:7]) #llo, 공백도 문자로 인식하기 때문임.
print(b[2:8]) #llo, W
#처음부터 슬라이스
print(b[:5]) #Hello
#끝까지 슬라이스
print(b[2:]) #llo, World

a = "Hello, World"
#upper()는 대문자로 모두 변경
print(a.upper()) #HELLO, WORLD
#lower()는 소문자로 모두 변경
print(a.lower()) #hello, world

# 문자열 바꾸기[변수.replace()]
a = "Hello, World"
print(a.replace("H","J")) #Jello, World

# 문자열 연결[문자열변수+문자열변수로 연결(+기호 사용)]
a = "Hello"
b = "World"
c = a + b
print(c) #HelloWorld
c = a + " " + b (문자열 사이에 공백 넣기-공백도 문자열로 인식함)
print(c) #Hello World




