**Spring IoC 컨테이너**

loc 컨테이너(Inversion of Control : 역제어컨테이너)

- 자바 객체(빈)의 라이프사이클(생성, 초기화, 서비스, 소멸)을 관리
- ContextLoaderListener(root) : 공유빈 관리
- DispathcerServlet : 개별빈 관리

----

**객체 만들어지는 순서(스프링)**

1. 객체 생성
2. 의존성 객체 주입
3. 의존성 객체 메소드 호출