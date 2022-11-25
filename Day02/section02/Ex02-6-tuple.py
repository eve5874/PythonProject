'''
튜플
   단일 변수에 여러 항목을 저장하는데 사용된다.
   순서가 있고, 변경할 수 없는 List
   둥근괄호로 작성된다.(리스트는 대괄호)
'''

thistuple = ("피카츄", "라이츄", "파이리")
print(thistuple)

#튜플길이 len()
print(len(thistuple)) #3
print(thistuple[1]) #라이츄
print(thistuple[-1]) #파이리
print(thistuple[1:3]) #('라이츄', '파이리')

#튜플값 변경 방법(튜플 값 변경 안되는데 굳이 하고 싶다면)-값 변경 안되는데 튜플사용하는 이유는 리스트보다 리소스사용이 적기 때문임.
thistuple = ("피카츄", "라이츄", "파이리")
thiscast = list(thistuple)
print(thiscast) #['피카츄', '라이츄', '파이리']
thiscast[1] = "잠만보"
thistuple = tuple(thiscast)
print(thistuple) #('피카츄', '잠만보', '파이리')

#튜플압축풀기
thistuple = ("피카츄", "라이츄", "파이리", "꼬부기")
(p1, p2, p3, p4) = thistuple
print(p1) #피카츄
print(p2) #라이츄
print(p3) #파이리
print(p4) #꼬부기

#두개 튜플 조인
thistuple1 = ("피카츄", "라이츄", "파이리", "꼬부기")
thistuple2 = ("버터플", "야도란", "피존투", "또가스")
thistuple3 = thistuple1 + thistuple2
print(thistuple3) #('피카츄', '라이츄', '파이리', '꼬부기', '버터플', '야도란', '피존투', '또가스')