console.log(a) // undefined !!
var a = 10
console.log(a)

// 선언만 끌어올리고(hoisting) 나머지 진행, 할당은 끌어올려지지 않음
// JS 가 이해한 코드(아래)
// var a   // <-- 선언과 초기화가 동시에 이루어짐
// console.log(a)
// a = 10   // <-- 할당
// console.log(a)
console.log('--------')

// let 은 위의 var 과 같이 할 수 없음!
// console.log(b)
// let b = 10
// console.log(b)

// 아래와 같은 과정을 거침
// let b    // <-- 선언 + TDZ
// console.log(b)   // 초기화가 되지 않아 'Cannot access 'b' before initialization'(ReferenceError) 발생
// b = 10   // <-- 할당 불가
// console.log(b)

console.log('--------')

if (x !== 1) {
  console.log(y) // undefined
  var y = 3
  if (y === 3) {
    var x = 1
  }
  console.log(y) // 3
}

if (x === 1) {
  console.log(y) // 3
}

// js 가 이해한 코드
// var x
// var y

// if (x !== 1) {
//   console.log(y) // undefined
//   var y = 3
//   if (y === 3) {
//     var x = 1
//   }
//   console.log(y) // 3
// }

// if (x === 1) {
//   console.log(y) // 3
// }

