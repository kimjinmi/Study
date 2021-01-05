#문자열
sentence = 'Python'
print(sentence)
sentence2 = "문자열2"
print(sentence2)
sentence3 = """
문자열1
문자열2
문자열3
"""
print(sentence3)

#슬라이싱
jumin = "990120-1234567"
print("성별 : "+ jumin[7])
print("년도 : " +jumin[0:2]) # 0,1
print("월 : " +jumin[2:4]) # 2,3
print("일 : " +jumin[4:6]) # 4,5

print("생년월일 : " + jumin[:6]) #~5
print("뒤 7자리 : " + jumin[7:]) #7~
print("뒤 7자리 (뒤에서 부터): " + jumin[-7:]) #맨뒤부터

#문자열처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)

index = python.index("n", index+1) # 두번째 n 찾기
print(index)

print(python.count("n"))

print(python.find("n"))
print(python.find("java")) # -1반환
# print(python.index("java")) # error

#문자열포맷
print("a" + "b")
print("a","b")

print("나는 %d살입니다." % 20)
print("나는 %s살입니다." % "스무살")
print("Apple은 %c로 시작해요" % "A")
print("나는 %s색과 %s색을 좋아함" % ("파란", "빨간"))

print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아함" .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아함" .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아함" .format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아함.".format(age=20, color="빨간"))

#Python v3.6~
age = 20
color ="빨간"
print(f"나는 {age}살이며, {color}색을 좋아함.")

#탈출문자
print("백문이 불여일견 \n백견이 불여일타")
print("Red\tApple")

print("백문이 '불여일견' 백견이 불여일타")
print('백문이 "불여일견" 백견이 불여일타')
print("백문이 \"불여일견\" 백견이 불여일타")
print("백문이 \'불여일견\' 백견이 불여일타")

print("D:\\PythonWorkspace>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스
print("Redd\bApple")



