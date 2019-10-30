// Array Helper Method
// 3. `.filter(callback())`
// 주어진 함수의 테스트를 통과한 모든 요소를 모아 새로운 배열로 반환
// 다시 말해 주어진 callback() 함수로 원하는 요소만 필터링 가능
// .map() 과 마찬가지로 원본을 변형시키지 않음

// for loop
var products = [
  { name: 'cucumber', type: 'vegetable' },
  { name: 'banana', type: 'fruit' },
  { name: 'carrot', type: 'vegetable' },
  { name: 'apple', type: 'fruit' },
]

var fruitProducts = []

for (var i = 0; i < products.length; i++) {
  if (products[i].type === 'fruit') {
    fruitProducts.push(products[i])
  }
}

console.log(fruitProducts)


// using `.filter()`
const PRODUCTS = [
  { name: 'cucumber', type: 'vegetable' },
  { name: 'banana', type: 'fruit' },
  { name: 'carrot', type: 'vegetable' },
  { name: 'apple', type: 'fruit' },
]

const FRUIT_PRODUCTS = PRODUCTS.filter(function (product) {
  return product.type === 'fruit'
  // 해당 조건이 true 면 return
})

// Refactoring 결과
// const FRUIT_PRODUCTS = PRODUCTS.filter( product => product.type === 'fruit' )

console.log(FRUIT_PRODUCTS)


// 3.3.1.
// users 배열에서 admin 레벨이 true 인 user object 들만 filteredUsers 에 저장하고 
// 배열의 두번째 유저의 이름을 출력
const users = [
  { id: 1, admin: false, name: 'justin'},  
  { id: 2, admin: false, name: 'harry' },
  { id: 3, admin: true, name: 'tak' },
  { id: 4, admin: false, name: 'jason' },
  { id: 5, admin: true, name: 'juan' },
]

// const filteredUsers = users.filter(function (user) {
//   return user.admin === true
// })

// Refactoring 결과
const filteredUsers = users.filter( user => user.admin === true )

console.log(filteredUsers)
console.log(filteredUsers[1].name)
