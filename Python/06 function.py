#전달값과 반환값
def open_account():
    print("새로운 계좌 생성")

def deposit(balance, money):
    print("입금 완료 {0}원".format(balance+money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금 완료. 잔액 : {0}".format(balance- money))
        return balance - money
    else :
        print("출금 완료 불가. 잔액 : {0}".format(balance))

def withdraw_nigth(balance, money):
    commission = 100
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 2000)
balance = withdraw(balance, 500)
commission, balance = withdraw_nigth(balance, 500)
print("수수료 : {0}, 잔액 : {1}".format(commission, balance))

#기본값
def profile(name, age=17, main_lang="파이썬"):
    print("이름 :{0}\t 나이:{1}\t 언어 : {2}" \
        .format(name, age, main_lang))

profile("A")
profile("B")

#키워드
profile(name="A", age=17, main_lang="파이썬")
profile(name="B", main_lang="파이썬", age=17)

#가변인자
def uselang(name, *language):
    print("이름 : {0}\t".format(name), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

uselang("A", "Python" , "java", "javascript", "C")
uselang("B", "Python" , "java")

#지역변수와 전역변수
gun = 10

def checkpoint(soldiers):
    global gun #전역변수
    gun = gun - soldiers
    print("남은 총 : {0}".format(gun))

def checkpoint_ret(gun, solders):
    gun = gun - solders
    print("남은 총 : {0}".format(gun))
    return gun

print("전체 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
