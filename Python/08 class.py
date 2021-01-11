### 클래스
class Unit:
    def __init__(self, name, hp, speed) :
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}".format(self.hp))
    
    def move(self, name, location) :
        print("{0} : {1} 방향으로 이동합니다. [속도:{2}]"\
            .format(self.name, location, self.speed))

marine1 = Unit("마린", 40, 5, 10)
marine2 = Unit("마린", 40, 5, 10)

### __init__ : 생성자
#marine3 = Unit("마린") 오류

### 멤버 변수 : 클래스 내애서 정의된 변수
wratih1 = Unit("레이스", 80, 5, 10)
wratih1.clocking = True
print("name : {0}, speed : {1}, clocking : {2}"\
    .format(wratih1.name, wratih1.speed, wratih1.clocking))

### 메소드
class AttackUnit : 
    def __init__(self, name, hp, speed, damage) :
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location) :
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.speed))
    
    def damaged(self, damage) :
        print("{0} : {1} 데미지를 잃었습니다.".format(self.name, speed))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)

### 상속 : Unit.__init__(self, name, hp, damage)

### 다중상속, 메소드 오버라이딩
class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location) :
        print("{0} : {1} 방향으로 날아갑니다. [속도:{2}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable) :
    def __init__(self, name, hp, damage, flying_speed) :
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)


valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

### pass
# class BuildingUnit(Unit) :
#     def __init__(self, name, hp, location):
#         pass # 아무것도 하지 않고 넘어감(오류X)

# def game_start():
#     pass

### super
class BuildingUnit(Unit) :
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0) # self 없이 상속받음
        self.location = location

class Unit :
    def __init__(self) :
        print("Unit 생성자")

class Flyable :
    def __init__(self) :
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit) :
    def __init__(self) :
        super().__init__ # Unit 생성자만 호출
        Unit.__init__(self)
        Flyable.__init__(self) # 명시적으로 두번해줘야함
