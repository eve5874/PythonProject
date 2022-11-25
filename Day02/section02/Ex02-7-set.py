'''
Set
   여러 데이터를 저장하는 객체이지만
   순서가 없다.
   변경할 수 없다.
   인덱싱되지 않는 컬렉션(데이터값을 여러개 갖는 것을 컬렉션이라 함)
   중괄호를 사용함
   중복값 없다
'''

thisset = {"피카츄", "라이츄", "파이리"}
#실행할 때마다 순서가 변경
print(thisset) #{'라이츄', '피카츄', '파이리'} 즉 불러올때는 순서 없이 불러옴(불러올때마다 순서가 계속 바뀜)

#항목 가져오기(항목을 하나씩 불러올 때는 순서가 없기 때문에 다음과 같이 함)
for x in thisset:
    print(x) #파이리
             #피카츄
             #라이츄
#->     thisset에 있는 항목을 하나씩 불러오는데 값이 안나올때까지 불러옴, 불러오는 순서는 계속 바뀔수있음(for은 반복문)

#값이 있는지 확인
thisset = {"피카츄", "라이츄", "파이리"}
print("피카츄" in thisset) #True
print("꼬부기" in thisset) #False

#항목추가하기
thisset.add("꼬부기")
print(thisset) #{'파이리', '라이츄', '꼬부기', '피카츄'} 꼬부기 추가 순서 지정못함

#다른 set 항목 추가1
thisset1 = {"피카츄", "라이츄", "파이리"}
thisset2 = {"꼬부기", "잠만보", "뮤츠"}
thisset1.update(thisset2)
print(thisset1) #{'잠만보', '뮤츠', '꼬부기', '피카츄', '파이리', '라이츄'} 순서는 섞임.

##다른 set 항목 추가2
thisset3 = {"피카츄", "라이츄", "파이리"}
thisset4 = {"꼬부기", "잠만보", "라이츄"}
thisset3.update(thisset4)
print(thisset3) #{'꼬부기', '피카츄', '파이리', '잠만보', '라이츄'} 라이츄는 중복값이라 하나만 들어감.

#항목제거1 (remove)
thisset = {"피카츄", "라이츄", "파이리"}
thisset.remove("피카츄")
print(thisset) #{'라이츄', '파이리'}
'''thisset.remove("피카츄") 
   print(thisset) 한번 더 하면 이미 없는 값을 지워달라고 한거라서 에러남. 
   그래서 discard쓸수있음
'''

#항목제거2 (discard는 여러번 명령해도 에러나지 않음)
thisset = {"피카츄", "라이츄", "파이리"}
thisset.discard("피카츄")
print(thisset) #{'라이츄', '파이리'}
thisset.discard("피카츄")
print(thisset) #{'라이츄', '파이리'}

#항목제거
thisset.pop() #순서가 없어서 무작위로 하나가 삭제됨

#비우기
thisset.clear()
print(thisset) #set()











