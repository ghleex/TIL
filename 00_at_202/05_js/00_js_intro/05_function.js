// 1. 선언식 (statement or declaration)
// 함수 선언식은 코드 실행 전 로드됨
// function add(num1, num2) {
//   return num1 + num2
// }

// console.log(add(2, 7))


// console.log('-------------------')
// // 2. 표현식 (expression)
// // 익명 함수를 특정 이름의 변수에 할당
// // 함수 표현식은 인터프리터(js)가 해당 코드에 도달했을 때 로드
// const sub = function(num1, num2) {
//   return num1 - num2
// }

// console.log(sub(7, 2))


// console.log('-------------------')
// // 함수도 하나의 값임
// console.log(typeof add)
// console.log(typeof sub)


// console.log('-------------------')
// // Arrow Function; 화살표 함수
// // 화살표 함수의 경우, 일반 function 키워드로 정의한 함수와 100% 동일한 것이 아님!
// // 화살표 함수는 항상 익명 함수임
// // 변수에 할당될 수 있으나, 이름 붙은 함수(생성자)로는 만들기 불가능
// const ssafy1 = function(name) {
//   return `hello, ${name}`
// }

// // 리팩토링(refactoring) - 화살표 함수로 줄여나가는 과정
// // 1. function 키워드 삭제
// const ssafy1 = (name) => {
//   return `hello, ${name}`
// }

// // 2. 매개변수의 `()` 소괄호 생략 (함수 매개변수가 하나일 경우에만)
// const ssafy1 = name => { return `hello, ${name}` }

// // 3. {} && return 생략 (함수 바디에 표현식이 하나일 경우만)
// const ssafy1 = name => `hello, ${name}`


// // Practicing Arrow Function Refactoring
// let square = function(num) {
//   return num ** 2
// }

// let square = (num) => { return num ** 2 }

// let square = num => { return num ** 2 }

// let square = num => num ** 2


// // 매개변수가 없는 경우
// let noArgs = () => 'No args'
// // 인자가 없기 때문에 소괄호 생략 못해
// // 그렇지만
// let noArgs = _ => 'No args'
// // 위와 같이 _ 사용할 수 있음


// // 객체(object)를 반환하는 경우
// let returnObject = () => { return {key: 'value'} }  // return 을 반드시 명시해야 함
// console.log(returnObject()) // { key: 'value' }


// // 객체(object) 반환하지만 return을 사용하지 않는 경우, 소괄호 사용
// let returnObject = () => ({key: 'value'})  // { key: 'value' }


// // 객체(object) 반환 시 문제가 되는 경우:
// // return 없는데 소괄호도 안 쓴 경우
// let returnObject = () => {key: 'value'}
// const test = returnObject()
// console.log(typeof test)  // undefined

// // 기본 매개변수를 줄 때는 매개변수 개수와 상관없이 무조건 소괄호 사용해야 함
// const sayHello = (name='noName') => `hi ${name}`


// Anonymous Function (익명 함수, 일회용 함수)
// 1. 기명 함수로 만들기 (변수 / 상수에 할당 ) - 생성과 동시에 함수의 인수로 할당
const cube = function(num) { return num ** 3 }   // 변수 할당
const squareRoot = num => num ** 0.5

console.log(cube(2))
console.log(squareRoot(4))


console.log('-----')
// 2. 익명 함수 즉시 실행
console.log((function (num) { return num ** 3 })(2))
console.log((num => num ** 0.5)(4))


// 함수 Hoisting
ssafy()

function ssafy() {
  console.log('hoisting!')
}

// 변수에 할당한 함수(표현식 형태)는 Hoisting 불가능
// 변수의 유효 범위(scope) 규칙을 따르기 때문
// let
ssafy2()

let ssafy2 = function () {
  console.log('hoisting!!')
}

// let(js가 이해한 코드)
let ssafy2  // 변수 선언

ssafy2()  // 함수 호출 -> ssafy2 는 초기화 되지 않았는데 함수 호출? 그렇다면 ReferenceError

ssafy2 = function () {
  console.log('hoisting!!')
} // 변수에 함수 할당


// var
ssafy3()

var ssafy3 = function () {
  console.log('hoisting!!!')
}

// var(js가 이해한 코드)
var ssafy3  // 1. 변수 선언 + 초기화

ssafy3()  // 2. 함수 호출 -> ssafy3 은 변수인데 함수 호출? ==> TypeError

ssafy3 = function () {
  console.log('hoisting!!!')
} // 3. 변수에 함수 할당
