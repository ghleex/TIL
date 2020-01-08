# WEB 과목평가 대비 정리

## 1. HTML

* HTML: Hyper Text Markup Language
  * 웹 페이지를 작성하기 위한 역할 표시 언어
* 웹 표준 만드는 곳: 현재까지는 W3C
  * WHATWG: HTML Living Standard
  * 앞으로 WHATWG에서 새롭게 표준 만들 것임
* HTML 요소: HTML 문서 최상위 요소로, root를 뜻함. head와 body로 구분
  * head: 문서 제목, 문자코드(인코딩)와 같이 해당 문서 정보를 담고 있으며, 브라우저에 나타나지 않음. CSS 선언 또는 외부 로딩 파일 지정 역시 가능
  * body: 브라우저 화면에 나타나는 정보로, 실제 내용에 해당

* sematic tag: 개발자와 브라우저가 사용하는 태그에 의미 부여
  * semantic tag를 사용함으로써 코드 가독성 높이고, 의도를 명확하게 만들 수 있다.
  * `<div>` 태그: non-sematic tag
  * `<table>`, `<article>`: sematic tag
  * sematic tag를 통해 태그 내 들어간 내용이 무엇인지 추측 가능!
  * 따라서 semantic tag는 해당 부분에만 사용하는 것이 좋다.
* PREVIOUSLY:

```html
<div class="header"> 
<div id="footer">
```

* HTML5:

```html
<header>이곳은 헤더입니다.</header>
<footer>이곳은 푸터입니다.</footer>
```





* 인용은 `<blockquote>`를 이용
* HTML5에서 추가된 시맨틱 태그: `<header>`, `<section>`, `<footer>`
* `<a>` 태그는 `href`로, `<img>` 태그는 `src` 를 통해 참조할 곳을 입력
* 상대 경로 입력 방법

```html
<img src="../Image/my_photo.png" alt="#">
```

* `<td>` 태그(table data)에서 셀 병합하기:
  * `rowspan`: 설정한 값 만큼 row를 커버한다는 의미
  * `colspan`: 설정한 값 만큼 column 커버한다는 의미
* 



## 2. CSS

* CSS: Cascading Style Sheets
* HTML과 CSS는 각자 문법을 가지는 별개 언어임
* 웹 브라우저는 내장 기본 스타일이 있어 CSS가 없어도 작동 함
* 자식 요소 프로퍼티는 부모의 프로퍼티를 모두 상속받지 않음: width, height, background-color 등 박스모델 관련 속성은 상속받지 않음
* HTML 최상위 요소의 사이즈를 기준으로 삼는 크기 단위: rem
* 후손(자손) 셀렉터(선택자): 해당 태그에 대하여 깊이에 상관없이 모두 적용시키고자 할 때 사용
* 자식 셀렉터(선택자): 해당 태그 바로 아래(indentation 하나 차이)에 있는 태그에 대하여 사용
* `#ssafy > p:nth-child(2)`와 `#ssafy > p:nth-of-type(2)`의 차이:
  * `태그명:nth-child(2)`: 자식 중 태그 상관없이 두 번째에 있는 자식에게 적용
  * `태그명:nth-of-type(2)`: 자식 중 해당 태그와 일치하는 두 번째 자식에게 적용

```html
<style>
    #ssafy > p:nth-child(2) {
        color: red;
    }
    #ssafy > p:nth-of-type(2) {
	color: blue;
	}
</style>
<div id="ssafy">
    <h2>어떻게 선택될까?</h2>
    <p>첫번째 단락</p>
    <p>두번째 단락</p>
    <p>세번째 단락</p>
    <p>네번째 단락</p>    
</div>
```

* `<ul>` 태그 아래 `<li>` 태그에 나타나는 불릿 모양 설정

```css
li {
  list-style-type: circle
  list-style-type: square
  list-style-type: none
      /* 위와 같이 다양하게 표현 가능 */
}
```





## 3. Bootstrap







## 4. 반응형 웹





