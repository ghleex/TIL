// 배열로 이루어진 숫자들을 모두 더하는 함수
const numberAddEach = numbers => {
  let sum = 0
  for (const number of numbers) {
    sum += number
  }
  return sum
}

// 배열로 이루어진 숫자들을 모두 빼는 함수
const numberSubEach = numbers => {
  let sub = 0
  for (const number of numbers) {
    sub -= number
  }
  return sub
}

// 배열로 이루어진 숫자들을 모두 곱하는 함수
const numberMulEach = numbers => {
  let mul = 0
  for (const number of numbers) {
    mul *= number
  }
  return mul
}

// 의문: 위와 같이 매번 함수를 정의해야할까?
// 공통된 기본 구조를 만들어보자
// 공통점: 배열로 이루어진 숫자들을 각각 [x] 한다
// [x] 를 callback 함수에서 처리하도록 바꾸어보자

// base template 역할하는 함수
const numbersEach = (numbers, callback) => {
  let acc
  for (const number of numbers) {
    acc = callback(number, acc)
  }
  return acc
}

// 기능별 callback 함수
const addEach = (number, acc = 0) => {
  return acc + number
}

const subEach = (number, acc = 0) => {
  return acc - number
}

const mulEach = (number, acc = 1) => {
  return acc * number
}

// 사용하기
const NUMBERS = [1, 2, 3, 4, 5,]
console.log('addEach')
console.log(numbersEach(NUMBERS, addEach))
console.log('subEach')
console.log(numbersEach(NUMBERS, subEach))
console.log('mulEach')
console.log(numbersEach(NUMBERS, mulEach))

// addEach, subEach, mulEach 는 다시 사용할 것 같지 않음..
// 그렇다면, numbersEach 이후 제어를 함수 정의 없이 매번 자유롭게 하려면 어떻게?
console.log(numbersEach(NUMBERS, (number, acc=0) => acc + number))
console.log(numbersEach(NUMBERS, (number, acc=0) => acc - number))
console.log(numbersEach(NUMBERS, (number, acc=1) => acc * number))
