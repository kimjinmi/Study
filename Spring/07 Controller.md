## Controller

**RequestMapping**

- HTTP 요청에 따라 요청 처리 및 Service로 처리 위임
- HTTP 응답 방법을 결정하고 뷰 이름을 리턴

- **Get/Post 모두 허용**
  - @RequestMapping

```java
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/ch02") // 공통부분 mapping
public class Ch02Controller {
	
	@RequestMapping("/content")
	public String content() {
		//요청처리
		return "ch02/content";
	}
}

```


- **GET 방식 허용**

```java
@RequestMapping(value="/getMethod", method=RequestMethod.GET)
public String getMethod() {
    logger.info("run");		
    return "ch02/content";
}

@GetMapping("/getMethod")
public String getMethod() {
    logger.info("run");		
    return "ch02/content";
}
```

- **POST 방식 허용**

```java
@RequestMapping(value="/postMethod", method=RequestMethod.POST)
public String postMethod() {
    logger.info("run");		
    return "ch02/content";
}

@PostMapping("/postMethod")
public String postMethod() {
    logger.info("run");		
    return "ch02/content";
}
```

- 같은 mapping을 요청해도 방식이 다르면 구분 가능

- **리턴타입**

  - ModelAndView : 뷰 이름 및 모델 정보를 전달
  - String : 뷰 이름을 전달
  - void : OutputStream, Writer를 이용해서 직접 응답 생성

- **요청 파라미터명과 동일한 매개변수 선언**	

  ```java
  @RequestMapping("/method1")
  public String method1(String param1, int param2, double param3, boolean param4, @DateTimeFormat(pattern="yyyy-MM-dd")Date param5) {
      //Integer.parseInt()로 강제 형변환 필요없이 숫자type으로 파라미터 받기 가능함
      //DateTimeFormat : parameter 넘어오는 pattern을 가지고 date객체로 변경하라고 안내
  
      return "ch03/content";
  }
  ```

- **요청 파라미터명과 매개변수명이 다른 경우**

  ```java
  @RequestMapping("/method2")
  public String method2(@RequestParam("param1") String arg1, @RequestParam("param2") int arg2,
                        @RequestParam("param3") double arg3,@RequestParam("param4") boolean arg4) {
  
      return "ch03/content";
  
  }
  ```

- **필수 요청 파라미터**

  ```java
  @RequestMapping("/method3")
  public String method3(@RequestParam(required = true) String param1, 
                        @RequestParam(required = true) String param2) {
  
      return "ch03/content";	
  }
  ```
  
- **Default 값**

  ```java
  @RequestMapping("/method4")
  	
  public String method4(@RequestParam(defaultValue = "")String param1, @RequestParam(defaultValue = "0") int param2, 
                        @RequestParam(defaultValue = "0.0") double param3, @RequestParam(defaultValue = "false") boolean param4) {
  
      //null->int로 변환 못해서 에러
  
      return "ch03/content";
  }
  ```

- **객체(Command Object)로 받기**

  ```java
  @RequestMapping("/method5")
  public String method5(Ch03Dto dto) {
  
  return "ch03/content";
  
  }
  ```