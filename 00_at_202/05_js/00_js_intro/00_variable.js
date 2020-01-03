// let(변수)
console.log('------ let ------')
let x = 1

if (x === 1) {
  let x = 2

  console.log(x) // 2
}
console.log(x) // 1


// const(상수)
console.log('------ const ------')

// const 선언 시 초기값 생략하면 오류 발생!
// const MY_FAV


const MY_FAV = 7

console.log('my favourite number is:' + MY_FAV)

// 상수 재할당 시도 시 오류 발생
// MY_FAV = 20

// 상수를 재선언 시도 시 오류 발생
// const MY_FAV = 20
// let MY_FAV = 20
// var MY_FAV = 20
console.log()


if (MY_FAV === 7) {
  // 블록 유효 범위(block scope)로 지정된 `MY_FAV` 라는 변수를 만들기 때문에 fine.
  // 즉, 전역변수가 아닌 특정 범위 내이므로 이름 공간 충돌이 발생하지 않음
  const MY_FAV = 20

  console.log('my favourite number is !!! ' + MY_FAV) // 20
}

console.log(MY_FAV) // 7


console.log('------ var ------')
// var (변수)
function varTest() {
  var x = 1
  if (true) {
    var x = 2
    console.log(x)  // 2, 상위 블록과 같은 변수
  }
  console.log(x) // 2
}
varTest()
console.log('--- varTest above / letTest below ---')
function letTest() {
  let x = 1
  if (true) {
    let x = 2
    console.log(x)  // 2, 상위 블록과 다른 변수
  }
  console.log(x)  // 1
}
letTest()

// let 과 var
console.log('--- let vs. var ---')
var a = 1
let b = 2

if (a === 1) {
  var a = 11
  let b = 22

  console.log(a)  // 11
  console.log(b)  // 22
}

console.log(a)  // 11
console.log(b)  // 2



console.log('----------------------')
// 식별자 작성 스타일
// 1. 카멜 케이스(camelCase) - 객체, 변수, 함수 (=== lower-camel-case)
let dog
let variableName // <-- camelCase

// 배열의 변수명은 복수형으로
const dogs = []

// 정규 표현식의 변수는 'r'로 시작
const rDecs

// 함수
function getPropertyName() {
  return 1
}

// boolean 반환하는 변수나 함수는 'is-' 로 시작
let isAvailable = false


// 2. 파스칼 케이스 (PascalCase) - 클래스, 생성자 (=== upper-camel-case)
class User {
  constructor(options) {
    this.name = options.name
  }
}


// 3. 대문자 스네이크 케이스 (SNAKE_CASE) - 상수
// 이 표현은 변수와 변수의 속성이 변하지 않는다는 것을 프로그래머에게 알려줌
const API_KEY = 'alksdjfjwe'
