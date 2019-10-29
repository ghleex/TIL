const a = 13
const b = -3
const c = 3.14  // float
const d = 2.998e8 // 2.998 * 10^8 = 299,800,000
const e = Infinity
const f = -Infinity
const g = NaN

console.log(a, b, c, d, e, f, g)


// 문자열 (Strings) 표현
const sentence1 = 'sentence'
const sentence2 = "sentence"
const sentence3 = `sentence`

// backtick(`)

// const word = "안녕
// 하세요"
// console.log(word)
// 따옴표는 줄바꿈 불가

const word1 = "안녕 \n하세요"
console.log(word1)

const word2 = `안녕
하세요`
console.log(word2)
// 줄바꿈 가능


// Template Literal (python 의 f-string과 유사)
// JS 에서 문자열을 입력하는 방식
const age = 10
const message = `홍길동은 ${age}
세입니다.`
console.log(message)


// 연산 가능 (덧셈만 가능하며 곱셈, 나눗셈, 뺄셈 불가)
const happy = 'hello'
const hacking = 'world' + 'lol' + '!!!'
console.log(happy, hacking)


// Boolean: true, false (python 과 대소문자 표기가 다름)

// Empty Value; NULL, undefined
// Number.isNan() 함수는 값이 NaN 여부 판단
// 주어진 값의 유형이 Number 이고 값이 NaN 이면 true, 아니면 false
Number.isNaN('ㅁㄴㅇ' + null)  // false; 
Number.isNaN(1 + null)  // false; 
Number.isNaN(1 + undefined) // true; 숫자이면서 NaN 모두 만족