## Controller

**Validation**

- validation 준비 내용

  - properties Editor Plugin

  - properties 파일 생성

  - 메세지를 관리하는 ResourceBundleMessageSource 빈 등록

    ```xml
    <!-- 에러 및 국제화 메세지를 관리하는 객체 -->
    	<bean id="messageSource"
    		class="org.springframework.context.support.ResourceBundleMessageSource">
    		<property name="basenames">
    			<list>
    				<!-- property파일의 이름, 언어는 제외(언어를 브라우저의 값에 맞춰서 스프링이 선택함) -->
    				<value>message.error</value>
    			</list>
    		</property>
    		<property name="defaultEncoding" value="UTF-8"/>
    	</bean>
    ```

  - Valid(폼 유효성 검사 요구)를 사용하기 위한 의존성 설정(pom.xml)

    ```xml
    <dependency>
        <groupId>javax.validation</groupId>
        <artifactId>validation-api</artifactId>
        <version>2.0.1.Final</version>
    </dependency>
    ```

  - Validator 클래스

    ```java
    import org.springframework.validation.Errors;
    import org.springframework.validation.Validator;
    import com.mycompany.webapp.dto.Ch04Member;
    
    public class Ch04MemberLoginFormValidator implements Validator {
    
    	@Override
    	public boolean supports(Class<?> clazz) {
    		boolean support = Ch04Member.class.isAssignableFrom(clazz); //Ch04Member클래스(+Member의 자식객체)로 할당할 수 있는가
    		return support;
    	}
    
    	@Override
    	public void validate(Object target, Errors errors) {
    		Ch04Member member = (Ch04Member) target;
    		//mid검사
    		if(member.getMid() == null || member.getMid().trim().equals("")) {
    			//올바른 값이 아니라고 등록 (문제 생긴 필드, error메세지의 key값)
    			//국제화를 위해 key값을 입력(서버가 브라우저에 맞춰서 error메세지 출력)
    			errors.rejectValue("mid", "errors.mid.required");
    		}else if(member.getMid().length() < 4){
    			//Object => 여러개의 다양한 값을 넣어주기 위해서(String, int, ..)알아서 박싱, 언박싱해줌
    			//{0},{1} => 순차적으로 object로 넘겨줌{아이디,4}
    			//만약에 property파일에 에러코드key가 없다면 "--"로 전해줌 
    			errors.rejectValue("mid", "errors.mid.minlength", new Object[] {4},"4자 이상");
    		}
        }
    }
    ```

  - Validator 설정

    ```java
    @PostMapping("/join")
    						//request범위에 joinForm이름으로 저장됨			error값을 받아옴(BindingResult = error)
    	public String join(@ModelAttribute("joinForm") @Valid Ch04Member member, BindingResult bindingResult) {
    		if(bindingResult.hasErrors()) {
    			//에러가 있을시(forward:JSP로 이동)
    			return "ch04/content";
    		} else {
    			//에러가 없을시(redirect:무조건 서블릿으로 다시 요청 // 위에 있는 content()로 요청처리함)
    			logger.info("run");
    			logger.info(member.getMid());
    			logger.info(member.getMpassword());
    			logger.info(member.getMemail());
    			logger.info(member.getMtel());
    			logger.info("회원가입이 처리됨");
    			return "redirect:/ch01/content";
    		}
    	}
    	
    
    //바인더 설정 변경(WebDataBinder:기본바인더)
    @InitBinder("joinForm")
    public void joinForm(WebDataBinder binder) {
    	binder.setValidator(new Ch04MemberJoinFormValidator());
    }
    ```

  - 에러메세지출력

    ```jsp
    <form method="post" action="join">
    	<input type="text" name="mid" class="form-control" value="${joinForm.mid}">
        <%--Spring MVC를 사용해야지 form --%>
    <form:errors cssClass="error" path="joinForm.mid"/>
    ```

    