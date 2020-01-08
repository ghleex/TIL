const me = {
  name: 'ssafy', // key 가 한 단어일 경우에는 '' 없이 사용 가능
  'phone number': '01098765432', // key 가 여러 단어로 구성 시 '' 로 묶어 사용
  appleProducts: {
    ipad: '2018pro',
    iphone: '7',
    macbook: '2019pro',
  }
}

console.log(me.name)  // ssafy
console.log(me['name']) // ssafy
console.log(me['phone number']) // 01098765432; 키가 여러 단어로 구성되어 있다면 반드시 [] 를 이용하여 접근


console.log(me.appleProducts) // { ipad: '2018pro', iphone: '7', macbook: '2019pro' }
console.log(me.appleProducts.ipad)  // 2018pro


// Object Literal (객체 표현법)
// ES5
var books = ['Learning JS', 'Eloquent JS']

var comics = {
  'DC': ['Joker', 'Aquaman'],
  'Marvel': ['Captain Marvel', 'Avengers'],
}

var magazines = null

var bookShop = {
  books: books,
  comics: comics,
  magazines: magazines,
}

console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.books[0])

// ES6+
// object 의 key 와 value 가 같다면, 배열과 같이 한 번만 작성 가능
let bookShop2 = {
  books,
  comics,
  magazines,
}
console.log(bookShop2)


console.log('------------')
// JSON
const jsonData = JSON.stringify({ // JSON 을 string 으로 변환
  coffee: 'Americano',
  iceCream: 'Mint Choco',  
})
console.log(jsonData) // '{"coffee":"Americano","iceCream":"Mint Choco"}'; 하나의 문자열로 출력
console.log(typeof jsonData)  // string

const parseData = JSON.parse(jsonData)
console.log(parseData)  // { coffee: 'Americano', iceCream: 'Mint Choco' }; object 형태
console.log(typeof parseData) // object
