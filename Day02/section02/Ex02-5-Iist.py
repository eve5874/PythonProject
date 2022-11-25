'''
List
    단일 변수에 여러 항목을 저장하는데 사용된다.
    List 항목은 순서가 지정되고(인덱스번호 있음) 변경가능하며 중복값 허용
    List 에는 다양한 데이터 유형이 포함될 수 있다.
'''
thislist = ["피카츄", "라이츄", "꼬부기"]
print(thislist) #['피카츄', '라이츄', '꼬부기']
print(thislist[0]) #피카츄
print(thislist[1]) #라이츄
#List 길이 [len(변수)]
print(len(thislist)) #3

#list 데이터 유형
list1 = ["피카츄", "라이츄", "꼬부기"]
list2 = [1,2,3,5]
list3 = [True, False, False]
#list에 들어가는 것은 다양한 유형 포함 가능(문자열,숫자 등)
list4 = ["abc", 34, False, 40]

#항목접근(인덱스번호로 항목에 접근가능)
thislist = ["피카츄", "라이츄", "꼬부기"]
print(thislist[1]) #라이츄

#변경[변수[변경할인덱스번호] = 변경원하는 값]
thislist = ["피카츄", "라이츄", "꼬부기"]
thislist[1] = '잠만보'
print(thislist) #['피카츄', '잠만보', '꼬부기']

#2개 항목 변경
thislist = ["피카츄", "라이츄", "꼬부기", "파이리", "버터플", "야도란"]
thislist[1:3] = ["울먹이","메타몽"]
print(thislist) #['피카츄', '울먹이', '메타몽', '파이리', '버터플', '야도란']

#두번째 세번째 값을 하나의 값으로 변경
thislist = ["피카츄", "라이츄", "꼬부기", "파이리", "버터플", "야도란"]
thislist[1:3] = ["울먹이"]
print(thislist) #['피카츄', '울먹이', '파이리', '버터플', '야도란']

#항목추가1 (맨 뒤에 붙여서 추가할 때 - 변수.append("추가항목"))
thislist = ["피카츄", "라이츄", "꼬부기"]
thislist.append("꼬부기")
print(thislist) #['피카츄', '라이츄', '꼬부기', '꼬부기']

#항목추가2 (중간에 추가할 때 - 변수.insert(인덱스번호, "추가항목")
thislist = ["피카츄", "라이츄", "꼬부기"]
thislist.insert(1,"잠만보")
print(thislist) #['피카츄', '잠만보', '라이츄', '꼬부기']

#항목 값으로 제거
thislist = ["피카츄", "라이츄", "꼬부기"]
thislist.remove("라이츄")
print(thislist) #['피카츄', '꼬부기']

#항목을 지정된 인덱스로 제거
thislist = ["피카츄", "라이츄", "꼬부기"]
thislist.pop(2)
print(thislist) #['피카츄', '라이츄']

#마지막 값만 제거
thislist = ["피카츄", "라이츄", "꼬부기"]
thislist.pop()
print(thislist) #['피카츄', '라이츄']

#목록삭제
thislist = ["피카츄", "라이츄", "꼬부기"]
thislist.clear()
print(thislist) #[] -> 값이 없는 것 뿐이지, 메모리 공간은 차지하는 상태임

#확장
thislist = ["피카츄", "라이츄", "꼬부기"]
thislist.extend(["버터플", "야도란"]) #대괄호는 list라는 표시임. 합집합처럼 합쳐짐
print(thislist) #['피카츄', '라이츄', '꼬부기', '버터플', '야도란']

#객체삭제 [del 리스트이름]
'''
list는 하나의 객체(object)임 여기 예시에서 thislist는 object임. object를 통해서 여러 기능을 사용할 수 있음.
 extend,clear,pop,remove이런 것도 list object라는 객체의 함수가 정의되어 있는 것임. 이를 매써드라고 함(객체에 종속된 함수를 매써드라함)
print는 객체가 아니라 내부에 저장된 함수라서 바로 불러와서 쓰는 함수임. 
"thislist.뭐시기()" 이런식으로  된 것은 "object.매써드()"임. 즉 extend,clear,pop,remove는 객체(object)에 종속된 함수임. 
list라는 객체가 메모리안에 올라가있는데 그 안에 값이 바뀔 수 있고 함수도 여러개 그룹핑되어 있는 것임
'''
# del thislist
# print(thislist)
'''#Traceback (most recent call last):
  File "C:\pstudy\PythonProject\Day02\section02\Ex02-5-Iist.py", line 84, in <module>
    print(thislist)
NameError: name 'thislist' is not defined
'''
#del 리스트 치면-> 위에 있는 thislist가 전부 사라지니까 값이 없어졌다고 위에 뜸.