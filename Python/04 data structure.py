# 리스트
subway = [10,20,30]


subway = ["A", "B", "C"]
print(subway.index("A")) # 0
subway.append("D") # ['A', 'B', 'C', 'D']
subway.insert(1, "E") # ['A', 'E', 'B', 'C', 'D']


print(subway.pop()) #['A', 'E', 'B', 'C']
subway.append("D")
print(subway.count("D"))
print(subway)

numlist = [4,5,3,2,1]
numlist.sort()
numlist.reverse() #내림차순 정렬
numlist.clear()
print(numlist)

mix_list = ["A", 20, True]
numlist = [4,5,3,2,1]
print(mix_list)
numlist.extend(mix_list) #합치기
print(numlist)

#사전
cabinet = {3:"A", 5:"D"}
print(cabinet[5])
print(cabinet.get(5))
# print(cabinet[10]) # 오류
print(cabinet.get(10)) # None
print(cabinet.get(10, "default")) # default

print(3 in cabinet) #True

cabinet_string = {"A-3":"A", "B-5":"D"}

cabinet_string["C-20"] ="E"
print(cabinet_string)

del cabinet_string["C-20"] # 삭제
print(cabinet_string)

print(cabinet_string.keys()) # dict_keys(['A-3', 'B-5'])
print(cabinet_string.values()) # dict_values(['A', 'D'])
print(cabinet_string.items()) # dict_items([('A-3', 'A'), ('B-5', 'D')])

cabinet_string.clear()

#튜플(내용변경 추가 X)
menu = ("A", "B")
# menu.add("C") #에러
print(menu)

(name, age, hobby) = ("A", 20, "C")
print(name, age, hobby)

#세트(중복 안됨, 순서 없음)
myset = {1,2,3,3,3}
print(myset)

java = {"a", "b", "c"}
python = set(["a", "d"])

print(java & python) # 교집합
print(java.intersection(python)) # 교집합

print(java | python) # 합집합
print(java.union(python)) #합집합

print(java - python)
print(java.difference(python))

python.add("b")
python.remove("b")
print(python)

#자료구조의 변경
menu = {"A", "B", "C"} # <class 'set'>
print(menu, type(menu)) 
menu = list(menu) # ['C', 'A', 'B']
menu = tuple(menu) # ('C', 'A', 'B') 
print(menu, type(menu)) 
