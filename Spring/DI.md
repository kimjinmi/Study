## DI(Dependency Injection) 의존 주입

1. Dependency Injection?

- 의존(Dependency) : 한 클래스가 다른 클래스의 메서드를 실행하는 것
- 사용 이유 : 모듈 간의 결합도를 낮춰서 유연한 변경을 가능하도록 하기 위하여
- DI : 의존에 의한 설계 패턴
  - 의존 객체를 외부에서 전달 받는 구현 형식
  - 웹 애플리케이션 구동시 자동으로 객체가 생성되고 관리
  - id 또는 name이 주어지지 않으면 클래스 이름의 첫자를 소문자로 한 이름 사용
  - 기본 생성자 필요(setter메소드를 이용한 의존성 주입)



2. xml 형식
   - 주로 외부 라이브러리 클래스를 이용할 경우 
   - 객체화 방법
     1. 기본 생성자 이용
     2. 기본 생성자가 없을 시 생성자 만드는 factory 메소드 (싱글톤형식)
3. Annotation 설정 방식
   - 객체 
     - @AutoWired(Field, Contructor, Setter)
     - @Resource(Field, Setter) : 제일 많이 사용
     - @Inject(Field, Contructor, Setter) : pom.xml 삽입 필요
   - 값
     - @Value(Field, Argument)
   - 인터페이스
     - @Autowired : 객체 설정전에 @Qualifier 설정 필요
     - @Resource
     - @Inject

