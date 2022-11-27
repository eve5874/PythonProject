'''
파일명 Ex04-6-conditions
조건연산자(삼항 연산자)
    참 if 조건식 else 거짓
    조건식 결과에 따라 참 또는 거짓의 결과를 반환한다.
    if와 else사이에 조건식이 들어가고 조건식이 참이면 참이 실행, 거짓이면 거짓이 실행
'''

a = 10
b = 20

result = (a - b) if (a >= b) else (b - a)
print('{}과 {}의 차이는 {}입니다.'.format(a, b, result))

