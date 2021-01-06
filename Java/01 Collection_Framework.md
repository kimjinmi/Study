### :pencil2: Collection_Framework​

**프레임워크**

- 사용 방법을 정해놓은 라이브러리
- 주요 인터페이스 : List, Set, Map



#### List 컬렉션

- 객체를 인덱스로 관리, 저장용량이 자동으로 증가함
- ArrayList, Vector, LinkedList 등 존재

- 주요 메소드
  - 객체 추가
    - boolean add(E e) : 객체를 맨 끝에 추가함
    - void add(int index, E e) : 주어진 인덱스에 객체를 추가함
    - E set(int index, E e) : 주어진 인덱스에 저장된 객체를 주어진 객체로 바꿈
  - 객체 검색
    - boolean contains(Object o) : 주어진 객체가 저장되어 있는지 조사
    - E get(int index) : 주어진 인덱스에 저장된 객체를 리턴
    - boolean isEmpty() : 컬렉션이 비어 있는지를 조사
    - int size() : 저장되어 있는 전체 객체 수를 조사
  - 객체 삭제
    - void clear() : 저장된 모든 객체를 삭제
    - E remove(int index)  : 주어진 인덱스에 저장된 객체를 삭제
    - boolean remove(Object o) : 주어진 객체를 삭제
- ArrayList(싱글스레드)
  - List<E> list = new ArrayList<E>();

- Vector(멀티스레드)
  - List<E> list = new Vector<E>();
- LinkedList
  - List<E> list = new LiinkedList<E>():



#### Set 컬렉션

- 순서가 상관없고, 중복이 허용되지 않음
- HashSet, LinkedHashSet, TrreSet 등 존재

- 주요 메소드

  - 객체 추가

    - boolean add(E e) : 객체를 저장함(성공시 true, 실패시 false)

  - 객체 검색

    - boolean contains(Object o) : 주어진 객체가 저장되어 있는지 조사
    - boolean isEmpty() : 컬렉션이 비어 있는지를 조사
    - Iterator<E> iterator()  : 저장된 객체를 한 번씩 가져오는 반복자 리턴
    - int size() : 저장되어 있는 전체 객체 수를 조사

  - 객체 삭제

    - void clear() : 저장된 모든 객체를 삭제
    - boolean remove(Object o) : 주어진 객체를 삭제

  - Iterator 인터페이스

    - boolean hasNext() : 가져올 객체가 있으면 true, 없으면 false
    - E next() : 컬렉션에서 하나의 객체를 가져옴
    - void remove() : Set 컬렉션에서 객체를 제거함

    ```java
    //일괄처리(방법1)
    for(String item : set) {
        System.out.println(item);
    }
    
    //일괄처리(방법2)
    Iterator<String> iterator = set.iterator();
    
    while(iterator.hasNext()) {
        String item = iterator.next();
        System.out.println(item);
    }
    ```

- HashSet

  - Set<E> set = new HashSet<E>();



#### Map 컬렉션

- Key와 Value로 구성된 Map.Entry 객체를 저장하는 구조
- Key는 중복저장X, Value는 중복 저장 가능
- HashMap, Hashtable, LinkedHashMap, Properties, TreeMap 등 존재

- 주요 메소드

  - 객체 추가

    - V put(K key, V value) : 주어진 키로 값을 저장함. 

      ​										새로운 키일 경우 null 리턴, 동일한 키가 있을경우 값 대체

  - 객체 검색

    - boolean containsKey(Object key) : 주어진 키가 저장되어 있는지 조사
    - boolean containsValue(Object value) : 주어진 값가 저장되어 있는지 조사
    - Set<Map.Entry<k,V>> entrySet()  : 키와 값의 쌍으로 구성된 모든 Map.Entry 객체를 Set에 담아 리턴
    - V get(Object key) : 주어진 키가 있는 값을 리턴
    - boolean isEmpty() : 컬렉션이 비어 있는지 확인
    - Set<k> keySet() : 모든 키를 Set 객체에 담아서 리턴
    - int size() : 저장된 키의 총 수를 리턴

  - 객체 삭제

    - void clear() : 저장된 모든 Map.Entry 객체를 삭제
    - V remove(Object key) : 주어진 Key와 일치하는 Map.Entry 객체 삭제, 값을 리턴

    ```java
    //일괄처리1
    Set<Integer> keySet = map.keySet();
    
    for(int key : keySet) {
        String value = map.get(key);
        System.out.println(key+":"+value);
    }
    				
    //일괄처리2
    Set<Entry<Integer, String>> entrySet = map.entrySet();
    
    for(Entry<Integer, String> entry : entrySet) {
        int key = entry.getKey();
        String value = entry.getValue();
        System.out.println(key+":"+value);
    }
    ```

- HashMap

  - Map<K, V> map = new HashMap<K, V>();



#### Stack

- LIFO : Last In First Out

- 주요 메소드
  - E push(E e) : 주어진 객체를 스택에 넣음
  - E peek() : 스택의 맨 위 객체를 가져옴. 객체를 스택에서 제거하지 않음
  - E pop() : 스택의 맨 위 객체를 가져옴. 객체를 스택에서 제거함
- Stack<E> stack = new Stack<E>();



#### Queue

- FIFO : First In First Out

- 주요 메소드
  - E offer(E e) : 주어진 객체를 큐에 넣음
  - E peek() : 큐의 맨 위 객체를 가져옴. 객체를 큐에서 제거하지 않음
  - E poll() : 큐의 맨 위 객체를 가져옴. 객체를 큐에서 제거함
- Queue<E> queue = new LinkedList<E>();