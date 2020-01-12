// const nothing = () => {
//   console.log('sleeping')
// }

// console.log('start')
// setTimeout(nothing, 3000)
// console.log('end')

// // start
// // end; 비동기식 처리
// // --- 3초 후 ---
// // sleeping
// console.log('----------')

// // setTimeout 대표적인 비동기 함수
// function sleep_3s() {
//   setTimeout ( () => console.log('wake up'), 3000 )
// }
// console.log('Start sleeping')
// sleep_3s()
// console.log('End of program')



// function first() {
//   console.log('first')
// }

// function second() {
//   console.log('second')
// }

// function third() {
//   console.log('third')
// }

// first()
// setTimeout(second, 1000)
// third()


console.log('Hi')

setTimeout(function ssafy() {
  console.log('ssafy')
}, 5000)

console.log('bye')


// function printHello() {
//   console.log('hello from baz')
// }

// function baz() {
//   setTimeout(printHello, 0)
// }

// function bar() {
//   baz()
// }

// function foo() {
//   bar()
// }

// foo()
