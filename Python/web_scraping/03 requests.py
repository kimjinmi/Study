import requests
res = requests.get("http://google.com")
res.raise_for_status() #문제시 오류, 프로그램 종료

# print("응답 코드 :", res.status_code) # 200 이면 정상, 403 접근권한 없음

# if res.status_code == requests.codes.ok:
#     print("정상")
# else :
#     print("에러코드 : ", res.status_code)

print(len(res.text))
print(res.text)

with open("mygoogle.html","w",encoding="utf-8") as f:
    f.write(res.text)