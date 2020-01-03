const numbers = [1, 2, 3, 4,]

console.log(numbers[0])   // 1
console.log(numbers[-1])  // undefined: 양의 정수 index 만 가능
console.log(numbers.length)   // 4

// reverse() 는 원본을 바꿔버림
console.log(numbers.reverse())
console.log(numbers)
console.log(numbers.reverse())
console.log(numbers)

// push; 배열의 길이를 반환
console.log(numbers.push('a'))  // 5
console.log(numbers)

// pop; 배열의 가장 마지막 요소를 제거함과 동시에 반환
console.log(numbers.pop())
console.log(numbers)

// unshift; 배열의 길이를 반환, 배열의 가장 첫 부분에 요소 삽입
console.log(numbers.unshift('a'))
console.log(numbers)

// shift; 배열의 가장 첫 요소를 제거함과 동시에 반환
console.log(numbers.shift())
console.log(numbers)

// include; boolean 반환, 해당 값 포함여부 판단
console.log(numbers.includes(1))
console.log(numbers.includes(0))


console.log(numbers.push('a', 'a'))
console.log(numbers)
console.log(numbers.indexOf('a')) // 4; 중복이 존재하는 경우 처음 찾은 요소의 index 반환
console.log(numbers.indexOf('b')) // -1; 찾을 요소가 없는 경우 -1 반환

// join - 배열의 요소를 join 함수의 인자를 기준으로 묶어 문자열로 반환
console.log(numbers.join()) // '1,2,3,4,a,a'; 인자가 없으면 쉼표(,) 기준으로 가져옴
console.log(numbers.join('')) // '1234aa'
console.log(numbers.join('-')) // '1-2-3-4-a-a'

console.log(numbers)  // [ 1, 2, 3, 4, 'a', 'a' ]; 원본을 바꾸지 않음
