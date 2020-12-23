## Transaction

**Transaction**

- All or Nothing 작업 처리

  

**Spring Transaction**

- 프로그래밍 방식과 선언적 방식 모두 지원
- 선언적 방식은 Spring AOP를 이용
  - RuntimeException이 발생시 자동 Rollback
  - Checked Exception 발생시 자동으로 Rollback 안됨

- 선언적인 방식은 Service 메소드 단위로 트랜잭션 처리



- 트랜잭션 관련 설정

```xml
<!-- 트랜잭션 관리자 객체 dataSource : db연결-->
<bean id="transactionManager"
	  class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
	<property name="dataSource" ref="dataSource"></property>
</bean>

<!-- 프로그래밍 방식을 위한 객체 -->
<bean id="transactionTemplate"
	  class="org.springframework.transaction.support.TransactionTemplate">
	<property name="transactionManager" ref="transactionManager" />	  
</bean>

<!-- 선언적 트랜잭션을 위한 설정(어노테이션) -->
<tx:annotation-driven transaction-manager="transactionManager"/> 

```


- 프로그래밍 방식

```java
	@Resource
	private TransactionTemplate transactionTemplate;

	public void transfer1(int fromAno, int toAno, int amount) {
		String result = transactionTemplate.execute(new TransactionCallback<String>() {

			@Override
			public String doInTransaction(TransactionStatus status) {
				try {
					//출금 작업
					Ch14Account fromAccount = accountDao.selectByAno(fromAno);
					if(fromAccount == null) {
						throw new Ch10NotFoundAccountException("출금계좌가 없음");
					}
					fromAccount.setBalance(fromAccount.getBalance() - amount);
					accountDao.updateBalance(fromAccount);
					
					//입금 작업
					Ch14Account toAccount = accountDao.selectByAno(toAno);
					if(toAccount == null) {
						throw new Ch10NotFoundAccountException("입금계좌가 없음");
					}
					toAccount.setBalance(toAccount.getBalance() + amount);
					accountDao.updateBalance(toAccount);
					
					return "success";
				} catch(Exception e) {
					logger.info(e.toString());
					status.setRollbackOnly(); //실패하면 rollback
					//컨트롤러에서 에러를 처리할 수 있도록 런타임예외 발생
					throw e;
				}
				
			}
			
		});
		
		if(result.equals("success")) {
			//성공했을때의 추가 내용
		}
	}
```

- 선언적 방식

```java
@Transactional
public void transfer2(int fromAno, int toAno, int amount) {
	//출금 작업
	Ch14Account fromAccount = accountDao.selectByAno(fromAno);
	if(fromAccount == null) {
		throw new Ch10NotFoundAccountException("출금계좌가 없음");
	}
	fromAccount.setBalance(fromAccount.getBalance() - amount);
	accountDao.updateBalance(fromAccount);
	//입금 작업
	Ch14Account toAccount = accountDao.selectByAno(toAno);
	if(toAccount == null) {
		throw new Ch10NotFoundAccountException("입금계좌가 없음");
	}
	toAccount.setBalance(toAccount.getBalance() + amount);
	accountDao.updateBalance(toAccount);
}
```