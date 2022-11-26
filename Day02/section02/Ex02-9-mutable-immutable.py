'''
mutable - 메모리 값을 변경가능한 객체
   리스트(list), 세트(set), 딕셔너리(dict)
'''

me = [1,2,3]
print(id(me)) #2810862753984 객체의 식별번호를 가져오는 것임. 주민등록번호나 학생반번호 같은 것임.
me.append(4)
print(id(me)) #위와 동일한 값이 나옴

'''
immutable - 메모리 값 변경불가
   정수(int), 실수(flaot), 문자열(str), 튜플(tuple)
'''
me = 10
print(id(me))
me += 1 # me = me + 1
print(id(me))
