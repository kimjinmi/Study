#### 표준입출력
print("python", "java", "javascript", sep=" , " , end="?")
print("AAAAAAAAAaa") # python , java , javascript?AAAAAAAAAaa

import sys
print("python", "java", file=sys.stdout) # 표준
print("python", "java", file=sys.stderr) # 에러처리

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): 
    print(subject.ljust(8), str(score).rjust(4), sep=":")
'''
수학      :   0
영어      :  50
코딩      : 100
'''
for num in range(1,11) :
    print("number : " + str(num).zfill(3))
'''
number : 001
number : 002
number : 003
number : 004
number : 005
number : 006
number : 007
number : 008
number : 009
number : 010
'''

#answer = input("Enter : ") # string 형태로 저장
#print("answer : "+ str(answer))

### 다양한 출력포맷

# 빈지리는 빈공간, 오른쪽 정렬, 총 10자리 공간을 확보
print("{0:>10}".format(500))
# 양수일땐 +, 음수 -
print("{0:>+10}".format(500))
print("{0:>+10}".format(-500))
# 왼쪽 정렬, 빈칸 _로 채움
print("{0:_<+10}".format(500))
# 세자리 마다 콤마, +- 부호 붙이기
print("{0:+,}".format(10000000000000))
# 세자리 마다 콤마, +- 부호 붙이기, 자릿수 확보, 빈자리 ^
print("{0:^<+30,}".format(10000000000000))

# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 3째 자리에서 반올림
print("{0:.2f}".format(5/3))

### 파일 입출력
score_file = open("score.txt", "w", encoding="utf-8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf-8")
score_file.write("과학 : 80")
score_file.write("\n사회 : 80")
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.read()) # 전체읽기
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="") # 한줄씩
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
while True:
    line = score_file.readline()
    if not line :
        break
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readline()
for line in lines:
    print(line, end="")
score_file.close()

###pickle
import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"A", "나이":30, "취미":["A","B","C"]}
print(profile)
pickle.dump(profile, profile_file) #profile에 있는 정보를 fil로 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file 에 있는 정보 profile에 불러오기
print(profile)
profile_file.close()

###with
import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf-8") as study_file:
    study_file.write("study")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())