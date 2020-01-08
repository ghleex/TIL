// Array Helper Method
// 5. .find(callback())
// 주어진 callback() 를 만족하는 첫 번째 요소 값만(여러 개 있더라도) 반환
// 없다면 undefined 반환
// 조건에 맞는 index 가 아닌, 요소 자체를 필요로 할 때 사용

// for
var users = [
  { name: 'Tony Stark', age: 45 },
  { name: 'Steve Rogers', age: 32 },
  { name: 'Thor', age: 40 },
  { name: 'Tony Stark', age: 23 },
]

// 원하는 object 를 찾아도 users 를 끝까지 돌게 됨
for (var i = 0; i < users.length; i++) {
  if (users[i].name === 'Tony Stark') {
    user = users[i]
    break // 원하는 조건에 도달하면 더 이상 루프를 돌지 않음
  }
}

console.log(user)

// find
const USERS = [
  { name: 'Tony Stark', age: 45 },
  { name: 'Steve Rogers', age: 32 },
  { name: 'Thor', age: 40 },
  { name: 'Tony Stark', age: 23 },
]

const newUser = USERS.find(function (user) {
  return user.name === 'Tony Stark'
})

// Refactoring
// const new_user = USERS.find( user => user.name === 'Tony Stark' )

console.log(newUser)