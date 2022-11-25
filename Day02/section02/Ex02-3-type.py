'''
내장 데이터 유형
    Python 변수는 다른 유형의 데이터를 저장할 수 있으며
    다른 표현은 다른 작업을 수행할 수 있다.
    텍스트 유형 : str
    숫자 유형 : int, float, complex
    시퀀스 유형 : list, tuple, range
    매핑 유형 : dict
    세트 유형 : set
    부울(논리) 유형 : bool
    바이너리 유형 : bytes, bytearray
    없음 유형 : NoneTpye
    '''
'''
시퀀스 유형 [A,B,C] 여러개 들어감. 들어가는 순서에 따라 번호가 매겨짐
매핑 유형 [key : value , key : value] 방식으로 매핑하는 것.
세트 유형 [A,B,C]여러개 들어감. 단, 들어가는 순서에 번호 매겨지지 않음.
부울 유형 True 나 False 두가지 값만 들어감. 스무고개하는 게임만들 때 예아니오 대답하는 경우 만듦. 특히 if 조건문
바이너리 유형 bytes단위로 숫자 등 byte단위값이 담기는 것
없음 유형은 파일 전송 복사할 때 바이너리타입으로 바꿔서 함.
변수 선언했는데 값이 없으면 그냥 NoneType이라고 나옴. (참고, 다른 언어에서는 null이라고 함.) 
'''

#str(텍스트유형)
x = "Hello, World"
print(type(x)) #<class 'str'>

#int(숫자유형-정수)
x = 20
print(type(x)) #<class 'int'>

#float(숫자유형-소수)
x = 20.5
print(type(x)) #<class 'float'>

#complex(숫자유형-복소수)
x = 1j
print(type(x)) #<class 'complex'>

#list(시퀀스 유형)
x = ["피카츄", "라이츄", "파이리"]
print(type(x)) #<class 'list'>

#tuple(시퀀스 유형)
x = ("피카츄", "라이츄", "파이리")
print(type(x)) #<class 'tuple'>

#range(시퀀스 유형)
x = range(6)
print(type(x)) #<class 'range'>

#dict(매핑 유형)
x = {"name":"피카츄", "기술":"백만볼트!"}
print(type(x)) #<class 'dict'>

#set(세트 유형)
x = {"피카츄", "라이츄", "파이리"}
print(type(x)) #<class 'set'>

#bool(논리유형)-True,False는 대문자로 시작
x = True
print(type(x)) #<class 'bool'>

#NoneType
x = None
print(type(x)) #<class 'NoneType'>
