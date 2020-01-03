### [컴포넌트] 

컴포넌트 이름: `my-todo-list`

컴포넌트 종류: 하고 싶은 일, 해야 하는 일로 구분되는 2개의 todo 리스트  

props로 app -> my-todo-list 로 데이터 내려주기



### [data Object] 

1. `todos` : 배열 
2. `newTodo`: 문자열 (추가 할 새로운 todo) 
3. `todayDate`: todo 작성 시각(Date() 내장 함수 사용)  
4. `titleColor`: 색상은 자유롭게  



### [methods]

1. `addTodo`  : todo를 등록하는 메서드
   - id  : 작성 시각 정보
   - content : 내용
   - completed : todo 유무 확인
   - todayDate : Date() 함수이용
2. `removeTodo`  :  특정 todo 삭제