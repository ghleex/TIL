// Array Helper Method
// 자주 사용하는 로직을 재활용할 수 있도록 미리 만들어진 라이브러리 같은 것

// 1. .forEach(callback())
// 주어진 callback 을 배열에 있는 각 요소에 대하여 오름차순으로 한 번씩 실행
// callback: 함수의 인자로 전달된 함수 / 추후 다룰 예정

// 1.1. ES5
var colors = ['red', 'blue', 'green']

for (var i = 0; i < colors.length; i++) {
  console.log(colors[i])
}

// 1.2. ES6+
const COLORS = ['red', 'blue', 'green']

COLORS.forEach(function (color) {
  console.log(color)
})

COLORS.forEach(color => console.log(color))

const result = COLORS.forEach(color => console.log(color))
console.log(typeof result)  // undefined; 반환 없음