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
  
    ```java
    import org.springframework.core.annotation.Order;
    import org.springframework.stereotype.Component;
    import org.aspectj.lang.annotation.Aspect;
    import org.aspectj.lang.annotation.Before;
    
    @Component
    @Aspect
    @Order(1) //순서
    public class Ch15Aspect1Before {
    
        @Before("execution(public * com.mycompany.webapp.controller.Ch15Controller.before(..))")
    	public void method() {
    		//전처리실행
    	}
    }
    ```
  
  - @After : 예외 발생 여부와 상관없이 핵심 로직을 호출한 후에 공통 기능을 실행
  
    ```java
    import org.springframework.stereotype.Component;
    import org.aspectj.lang.annotation.After;
    import org.aspectj.lang.annotation.Aspect
    @Component
    @Aspect
    public class Ch15Aspect3After {
    
    	@After("execution(public * com.mycompany.webapp.controller.Ch15Controller.After(..))")
    	public void method() {
    		//후처리실행
    	}
    }
    ```
  
  - @AfterReturning : 핵심 로직이 예외 없이 실행해야만 공통 기능을 수행
  
    ```java
    import org.aspectj.lang.annotation.AfterReturning;
    import org.aspectj.lang.annotation.Aspect;
    import org.springframework.stereotype.Component;
    @Component
    @Aspect
    public class Ch15Aspect4AfterReturning {
    
    @AfterReturning("execution(public * com.mycompany.webapp.controller.Ch15Controller.afterReturning(..))")
        public void method() {
            //후처리실행
        }
    }
    ```
  
  - @AfterThrowing : 핵심 로직이 예외를 발생시킬 때 공통 기능을 수행
  
    ```java
    import org.aspectj.lang.annotation.AfterThrowing;
    import org.aspectj.lang.annotation.Aspect;
    import org.springframework.stereotype.Component;
    @Component
    @Aspect
    public class Ch15Aspect5AfterThrowing {
    	
        @AfterThrowing(
                pointcut = "execution(public * com.mycompany.webapp.controller.Ch15Controller.afterThrowing(..))", throwing = "ex")
        public void method(Throwable ex) {//exception이 상속하는 throwable
            logger.info("후처리 실행");
            logger.info(ex.toString());
        }
    }
    ```
  
  - @Around : 핵심 로직을 호출하기 전과 후에 공통 기능을 실행
  
    ```java
    import org.springframework.stereotype.Component;
    import org.aspectj.lang.ProceedingJoinPoint;
    import org.aspectj.lang.annotation.Around;
    import org.aspectj.lang.annotation.Aspect;
    @Component
    @Aspect
    public class Ch15Aspect6Around {
        
    	@Around("execution(public * com.mycompany.webapp.controller.Ch15Controller.around(..))")
    	public Object method(ProceedingJoinPoint joinPoint) throws Throwable{
    		//전처리
    		String methodName = joinPoint.getSignature().toShortString();
    		//-------
    		Object result = joinPoint.proceed();
    		//-------
    		//후처리
    		return result;
    	}
    }
    ```
  
    



