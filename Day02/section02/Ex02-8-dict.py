'''
Dictionary
  key:value로 이루어져 쌍으로 데이터 값을 저장하는데 사용
  리스트는 인덱스 번호 생겨서 인덱스번호로 참조할 수 있음.
'''

#dictionary선언
thisdict = {
    "brand" : "구찌",
    "model" : "g001",
    "year" : 2022
}
print(thisdict) #{'brand': '구찌', 'model': 'g001', 'year': 2022}

'''
키 이름을 사용하여 참조할 수 있다. 
'''

#값가져오기
thisdict = {
    "brand" : "구찌",
    "model" : "g001",
    "year" : 2022
}
print(thisdict["brand"]) #구찌
print(thisdict.get("model")) #g001

# 키 목록 가져오기
print(thisdict.keys()) #dict_keys(['brand', 'model', 'year'])->리스트로 가져옴

#추가하기
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict["color"] = "red"
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
thisdict.update({"bgColor" : "black"})
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red', 'bgColor': 'black'}

#변경하기
thisdict["color"] = "yellow"
thisdict.update({"bgColor" : "blue"})
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'yellow', 'bgColor': 'blue'}

#제거하기
thisdict.pop("model")
print(thisdict) #{'brand': 'Ford', 'year': 1964, 'color': 'yellow', 'bgColor': 'blue'}

#마지막 삽입된 항목 제거하기
thisdict.popitem()
print(thisdict) #{'brand': 'Ford', 'year': 1964, 'color': 'yellow'}













