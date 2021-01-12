### 예외 처리
try :
    nums = []
    nums.append(int(input("num 1 :")))
    nums.append(int(input("num 2 :")))
    nums.append(int(nums[0]/nums[1]))
    print("result : {2}".format(nums[2]))
except ValueError:
    print("error, value")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)

### 에러 발생시키기
try :
    num1 = int(input("num 1 :"))
    num2 = int(input("num 2 :"))
    if num1 >= 10 or num2 >- 10:
        raise ValueError
    print("result : {2}".format(int(num1/num2)))
except ValueError:
    print("잘못된 값 입력")

### 사용자 정의 예외처리
class BigNumberError(Exception):
    def __init__(self, msg) :
        self.msg = msg
    
    def __str__(self):
        return self.msg

try :
    num1 = int(input("num 1 :"))
    num2 = int(input("num 2 :"))
    if num1 >= 10 or num2 >- 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("result : {2}".format(int(num1/num2)))
except ValueError:
    print("err, 잘못된 값 입력")
except BigNumberError as err:
    print("err, 한자리 값 입력")
    print(err)
finally:
    print("end")

### finally : 무조건 실행