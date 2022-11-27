'''
Ex07-2-for-range.py

for문과 range함수
'''

dan = int(input('출력할 구구단을 입력하시오. >>>'))
for n in range(1,10):
    print('{}x{}={}'.format(dan, n, dan * n))


#range(1,10)은 범위가 1부터 9까지
#range(10)으로 적으면 0부터 9까지
#range(1,10,2)은 마지막에 2가 스텝으로 기능해서 1,3,5,7,9로 끊겨서 나옴
'''
range()
    연속된 숫자를 만들어주는 함수 
'''
'''
range(stop)
'''
# 0~9 range
for n in range(10):
    print('{}x{}={}'.format(dan, n, dan * n), end='')

'''
range(start,stop)
'''
# 1~9 range
for n in range(1,10):
    print('{}x{}={}'.format(dan, n, dan * n), end='')

'''
range(start,stop,step)
'''
# 1부터 2씩 증가 < 10 (1,3,5,7,9)
for n in range(1,10,2):
    print('{}x{}={}'.format(dan, n, dan * n), end='')