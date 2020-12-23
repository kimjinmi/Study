## AOP(Aspect Oriented Programming) 관점 지향 프로그래밍

- 공통 관심사를 핵심 관심사(Core)로부터 분리하여 코드 중복을 해소
- 핵심 관심사 수정 없이 공통 관심사만 별도로 변경 가능함
- 클래스를 시작하기전 **@Aspect**필요
- AOP 용어
  - Aspect : 공통 관심사
  - Advice : 공통 코드 삽입 위치(핵심로직 전/후)
  - JointPoint : 핵심 로직의 호출 지점 
  - Pointcut : Aspect를 적용할 핵심 코드(메소드)를 지정
  - Weaving : 공통 코드를 핵심 로직에 적용하는 것

- Advice 종류
  - @Before : 핵심 로직을 호출하기 전에 공통 기능을 수행
  - @After : 예외 발생 여부와 상관없이 핵심 로직을 호출한 후에 공통 기능을 실행
  - @AfterReturning : 핵심 로직이 예외 없이 실행해야만 공통 기능을 수행
  - @AfterThrowing : 핵심 로직이 예외를 발생시킬 때 공통 기능을 수행
  - @Around : 핵심 로직을 호출하기 전과 후에 공통 기능을 실행