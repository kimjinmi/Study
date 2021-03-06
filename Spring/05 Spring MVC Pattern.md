## Spring MVC Pattern

**MVC**

- **모델-뷰-컨트롤러**(Model–View–Controller, MVC)
- 사용자 인터페이스로부터 비즈니스 로직을 분리하여 애플리케이션의 시각적 요소나 그 이면에서 실행되는 비즈니스 로직을 서로 영향 없이 쉽게 고칠 수 있음
- Model : 모델의 상태에 변화가 있을 때 컨트롤러와 뷰에 이를 통보함
- View : 사용자가 볼 결과물을 생성하기 위해 모델로부터 정보 얻어 옴.
- Controller : 모델에 명령을 보냄으로써 모델의 상태를 변경할 수 있음.



![mvc pattern](https://github.com/kimjinmi/Study/blob/main/repository/mvc.PNG)



**스프링 MVC의 주요 구성 요소**

1. DispatcherServlet : 클라이언트의 요청을 전달받음. 컨트롤러에게 클라이언트의 요청을 전달하고, 컨트롤러가 리턴한 결과값을 View에 전달하여 알맞은 응답을 생성하도록 한다.
2. HandlerMapping : 클라이언트의 요청 URL을 어떤 컨트롤러가 처리할지 결정
3. Controller : 클라이언트의 요청을 처리한 뒤, 결과를 리턴한다. 응답 결과에서 보여줄 데이터를 모델에 담아 전달함.
4. ViewResolver : 컨트롤러의 처리 결과를 보여줄 뷰를 결정함.
5. View : 컨트롤러의 처리 결과 화면을 생성한다. JSP 등을 이용하여 클라이언트에 응답 결과를 전송한다.
6. Service : 비즈니스 로직(컴퓨터 프로그램에서 실세계의 규칙에 따라 데이터를 생성·표시·저장·변경하는 부분)을 수행함.

