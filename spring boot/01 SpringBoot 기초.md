- 참고 : https://goddaehee.tistory.com/, https://badstorage.tistory.com/

- 스프링 부트?

  - 스프링 프레임워크를 사용하는 프로젝트를 간편하게 설정할 수 있는 스프링 프레임워크의 서브 프로젝트

- 스프링 부트 장점

  - 빠른 프로젝트 개발 가능
  - 비기능적인 기능 기본적 제공

- 접속 : https://start.spring.io/

-  Help -> Eclipse MarketPlace -> STS4설치

- pom.xml

  ```xml
  <properties><!-- 자바 버전 관리 -->
      <java.version>1.8</java.version>
  </properties>
  
  <dependencies><!-- 의존성 관리 -->
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter</artifactId>
      </dependency>
  
      <dependency>
          <groupId>org.springframework.boot</groupId>
          <artifactId>spring-boot-starter-test</artifactId>
          <scope>test</scope>
      </dependency>
  </dependencies>
  
  <build><!-- 빌드 플러그인 관리 -->
      <plugins>
          <plugin>
              <groupId>org.springframework.boot</groupId>
              <artifactId>spring-boot-maven-plugin</artifactId>
          </plugin>
      </plugins>
  </build>
  ```

- @SpringBootApplication

  - 해당 어노테이션 하나가 @EnableAutoConfiguration, @ComponentScan, @Configuration
  - 해당 annotation을 설정한 클래스가 있는 package를 최상위 패키지로 인식하고 ComponentScan을 수행

- spring Boot DevTools : https://hojonglee.github.io/2017-08-01/Developer_tools

- https://m.blog.naver.com/bb_/222141978468