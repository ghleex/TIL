// while
let i = 0

while (i < 6) {
  console.log(i)
  i++
}


console.log('----------')
// for
for (let j = 0; j < 6; j++) {
  console.log(j)
}

console.log('---')
const numbers = [0, 1, 2, 3, 4, 5,]
for (let number of numbers) {
  console.log(number)
}
console.log('-')
for (let number of [0, 1, 2, 3, 4, 5,]) {
  console.log(number)
}
console.log('-')
for (const number of [0, 1, 2, 3, 4, 5,]) {
  console.log(number)
}