// if 문
const userName = 'ssafy'

if (userName === '1q2w3e4r') {
  message = '<h1>This is admin page</h1>'
} else if (userName === 'ssafy') {
  message = '<h1>You are from ssafy</h1>'
} else {
  message = `<h1>hello ${userName}</h1>`
}


// switch - case 문
switch (userName) {
  case '1q2w3e4r': {
    message = '<h1>this is admin</h1>'
    break
  }
  case 'ssafy': {
    message = '<h1>You are from ssafy</h1>'
    break
  }
  default: {
    message = `<h1>hello ${userName}</h1>`
  }
}
