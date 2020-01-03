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


// 1.1.1. 연습
// 객체, id, 
function handlePosts() {
  const posts = [
    {id: 23, title: 'News'},
    {id: 52, title: 'Code City'},
    {id: 102, title: 'Python'},
  ]

  // for (let i = 0; i < posts.length; i++) {
  //   console.log(posts[i])
  //   console.log(posts[i].id)
  //   console.log(posts[i].title)
  // }

  posts.forEach(function (post) {
    console.log(post)
    console.log(post.id)
    console.log(post.title)
  })

  // posts.forEach(post => {
  //   console.log(post)
  //   console.log(post.id)
  //   console.log(post.title)
  // })
  
}
handlePosts()

// 1.1.2. 연습
// images 배열 안에 있는 정보를 곱해 넓이를 구하고, areas 배열에 저장
const images = [
  { height: 10, width: 30 },
  { height: 20, width: 90 },
  { height: 54, width: 32 },
]

const areas = []
images.forEach(function (image) {
  areas.push(image.height * image.width)
})
// images.forEach( image => areas.push(image.height * image.width) )

console.log(areas)
