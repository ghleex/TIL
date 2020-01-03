// Array Helper Method
// 6. `.some(callback())`
// 배열 안의 어떤 요소라도(하나라도) 주어진 callback() 를 통과하는지 테스트 후
// 결과에 따라 boolean 반환
// 빈 배열은 무조건 false 반환
// 조건에 맞는 요소를 찾는 즉시 검색 멈추고 true 반환
// `||` 연산(OR)과 유사

const arr = [1, 2, 3, 4, 5,]
const result = arr.some( elem => elem % 2 === 0 )

console.log(result)


// 7. `.every(callback())`
// 배열 안의 모든 요소가 주어진 callback() 를 통과하는지 테스트 후
// 결과에 따라 boolean 반환
// 빈 배열은 무조건 true 반환
// 배열의 모든 요소가 조건에 맞아야 true, 하나라도 맞지 않으면 false
// 조건에 맞지 않는 요소를 찾는 즉시 검색 멈추고 false 반환
// `&&` 연산(AND)과 유사

const result2 = arr.every( elem => elem % 2 === 0 )

console.log(result2)

// 7.1. 연습
// for loop
// ram 이 16보다 작으면 everyComputers 를 false 로, 
// 아니면 someComputers 를 true 로

var everyComputers = true
var someComputers = false

var computers = [
  { name: 'macbook', ram: 8 },
  { name: 'gram', ram: 16 },
  { name: 'series9', ram: 32 },
]

for (var i = 0; i < computers.length; i++) {
  var computer = computers[i]

  if (computer.ram < 32) {
    everyComputers = false
  } else {
    someComputers = true
  }
}

console.log(everyComputers) // false
console.log(someComputers)  // true


// some / every
const COMPUTERS = [
  { name: 'macbook', ram: 8 },
  { name: 'gram', ram: 16 },
  { name: 'series9', ram: 32 },
]

// some
const SOME_COMPUTERS = COMPUTERS.some( computer => computer.ram < 32 )
console.log(SOME_COMPUTERS)

// every
const EVERY_COMPUTERS = COMPUTERS.every( computer => computer.ram < 32 )
console.log(EVERY_COMPUTERS)