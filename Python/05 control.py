#if
weather = input("오늘 날씨는 ? ")
if weather == "비" or weather == "눈" :
    print("우산 챙김")
elif weather == "미세먼지":
    print("마스크 챙김")
else :
    print("둘다 필요 없음")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더움")
elif 10 <= temp < 30 :
    print("괜찮은 날씨")
else :
    print("너무 추움")

# for
for waiting_no in range(1, 5):
    print("대기번호 :{0}".format(waiting_no)) # 1~4

list = ["A", "B", "C"]
for item in list:
    print("number : {0}".format(item))

#while
str = "A"
index = 5
while index >=1:
    print("{0}. order : {1}".format(str,index))
    index -= 1
    if index == 0:
        print("last order")

while True:
    print("{0}, order : {1}".format(str, index))
    index += 1
ctrl + c :종료

strbefor = "A"
strafter = "Unknown"

while strafter != strbefor :
    print("{0}, order".format(strbefor))
    strafter = input("order?")

#continue 와 break
absent =[2,5]
no_num = [7]
for student in range(1, 11):
    if student in absent:
        continue
    if student in no_num:
        print("end : {0}" .format(student))
        break
    print("number : {0}".format(student))

#한 줄 for
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

str_for = ["AAAAA", "BBB", "CC CC"]
str_for = [len(i) for i in str_for]
print(str_for)