'''
대입 연산자
    변수에 값을 저장하기 위해 사용하는 연산자
print 형식문자
    %d : 숫자데이터
    %f : 실수데이터
    %0 : 8진수 데이터
    %x : 16진수 데이터
    %s : 문자열 데이터
    %c : 문자 하나 데이터
'''

a,b = 10,20
print('a = %d, b = %d' % (a,b)) #a = 10, b = 20
a,b=b,a
print('a = %d, b = %d' % (a,b)) #a = 20, b = 10

#복합대입연산자
'''
    +=
        ex) x += 3 과 x = x + 3과 같다.
    _=
        ex) x -+ 3 과 x = x - 3과 같다.

'''

piggy_bank = 0
money = 10000
piggy_bank += money
print(money) #10000

print("지금 저금통에 용돈 {}원을 넣었습니다.".format(money))
print('지금 저금통에는 {}원이 있습니다.'.format(piggy_bank))

snack=2000
piggy_bank-= snack
print('저금통에서 스낵 구입비 {}원을 뺐습니다.'.format(snack)) #저금통에서 스낵 구입비 2000원을 뺐습니다.
print('지금 저금통에는 {}원이 있습니다.'.format(piggy_bank)) #지금 저금통에는 8000원이 있습니다.