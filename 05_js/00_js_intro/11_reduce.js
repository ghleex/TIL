// Array Helper Method
// 4. `.reduce(callback())`
// 배열의 각 요소에 대하여 주어진 reduce() 함수를 실행 후
// 하나의 결과 값을 반환
// reduce() 는 배열 내 숫자 총 합, 평균 등과 같이 배열 내 값들을 하나로 줄이는 동작 수행
// map 은 배열의 각 요소를 변형한다면, reduce 는 배열 자체를 변형시킴
// 배열 전체를 기준으로 동작

// 총 합
const ssafyTests = [90, 90, 80, 77,]
const sum = ssafyTests.reduce(function (total, x) {
  return total += x
  // return 이 있는 경우 total += x, 0 불가능 ==> 0 으로 나옴
})
// const sum = ssafyTests.reduce(function (total, x) {
//   return total += x
//   // return 이 있는 경우 total += x, 0 불가능 ==> 0 으로 나옴
// }, 0)

// Refactoring 결과
// const sum = ssafyTests.reduce( (total, x) => total += x, 0 )
// const sum = ssafyTests.reduce( (total, x) => total += x )

console.log(sum)
// callback() 의 첫 번째 매개변수는 누적값(전 단계의 결과; total)
// 두 번째 매개변수(x)는 현재 배열 요소, 현재 인덱스, 배열 자체 순
// 초기값 === 0 (첫 total 값)
// 초기값이 생략되면 배열의 첫 번째 요소가 초기값이 됨


// 4.1. 연습
// 주어진 배열 내 모든 요소의 합을 구하시오
const arr = [0, 1, 2, 3,]
const summy = arr.reduce(function (total, x) {
  return total += x
 }, 0)

// Refactoring 결과
// const summy = arr.reduce( (total, x) => total += x, 0 )
console.log(summy)