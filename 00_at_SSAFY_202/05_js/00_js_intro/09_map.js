// Array Helper Method
// 2. .map(callback())
// 배열 내의 모든 요소에 대하여
// 각각 주어진 함수(callback())를 호출한 결과를 모아 새로운 배열을 반환하거나
// 일정 형식의 배열을 다른 형식으로 바꾸어야 할 때 사용

// 2.1. for loop
var numbers = [1, 2, 3,]
var doubleNumbers = []

for (var i = 0; i < numbers.length; i++) {
  doubleNumbers.push(numbers[i] * 2)
}

console.log(doubleNumbers)  // [ 2, 4, 6 ]
console.log(numbers)  // [ 1, 2, 3 ]; 원본 변형 없음


// 2.2. map
const NUMBERS = [1, 2, 3,]
const DOUBLE_NUMBERS = NUMBERS.map(function (number) {
  return number * 2
})
console.log(DOUBLE_NUMBERS) // [ 2, 4, 6 ]
console.log(NUMBERS)  // [ 1, 2, 3 ]

// refactoring
// const DOUBLE_NUMBERS = NUMBERS.map( number => number * 2 )

// 2.2.1. 연습
const newNumbers = [4, 9, 16,]
const roots = newNumbers.map(Math.sqrt)

console.log(roots)

// 2.2.2.
// map 을 사용하여 images 배열 안의  Object 들의 height 값만 저장되어 있는 heights 배열을 만드시오.
const images = [
  { height: '34px', width: '39px' },
  { height: '12px', width: '11px' },
  { height: '292px', width: '56px' },
]

const heights = images.map(function (image) {
  return image.height
})

// Refactoring 결과
// const heights = images.map(image => image.height)

console.log(heights)

// 2.2.3.
// map 을 사용하여 trips 배열의 값들을 계산한 결과인 속도 값을 저장하는 배열 sppeds 를 만드시오.
const trips = [
  { distance: 35, time: 10 },
  { distance: 90, time: 10 },
  { distance: 60, time: 25 },
]

const speeds = trips.map(function (trip) {
  return trip.distance / trip.time
})

// Refactoring 결과
// const speeds = trips.map( trip => trip.distance / trip.time )

console.log(speeds)

// 2.2.4.
const brands = ['Marvel', 'DC',]
const movies = ['IronMan', 'Batman',]

const comics = brands.map(function (x, i) {
  return { name: x, hero: movies[i] }
})

// Refactoring 결과
// const comics = brands.map( (x, i) => ({ name: x, hero: movies[i]}) )

console.log(comics)
// [
//   { name: 'Marvel', hero: 'IronMan'},
//   { name: 'DC', hero: 'Batman'},
// ]
