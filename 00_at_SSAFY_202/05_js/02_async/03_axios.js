const axios = require('axios')

axios.get('http://jsonplaceholder.typicode.com/poss')
  .then(response => {
    console.log(response) 
  })
  .catch(err => { 
    console.log(err) 
  })
