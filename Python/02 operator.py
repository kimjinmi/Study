#연산자
print(2**3) # 2^3
print(5%3) # 나머지
print(5//3) # 몫

print(5<=8)
print(3==3) # equal
print(3+4 != 7) # not equal
print(not(1 != 3))

print((3>0) and (3<5))
print((3>0) & (3<5))

print((3>0) or (3>5))
print((3>0) | (3>5))
print(5>4>3)

#수식
print(2+3*4)
print((2+3)*4)
number = 2+3*4
print(number)
number = number +2
number += 2
number *= 2
number %= 5
print(number)

#숫자처리함수
print(abs(-5)) # 5
print(pow(4,2)) # 4^2
print(max(5,12)) # 12
print(min(5,12)) # 5
print(round(3.14)) #3
print(round(4.99)) #5

from math import *
print(floor(4.99)) # 내림4
print(ceil(3.14)) # 올림4
print(sqrt(16)) # 제곱근4

#랜덤함수
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)
print(int(random()*10)) # 0 ~ 9
print(int(random()*10)+1) # 1 ~ 10

#로또구하기
print(int(random() * 45) + 1)

print(randrange(1,46)) # 1~45

print(randint(1,45)) # 1~45