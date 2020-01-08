// webpack 설정 파일
const VueLoaderPlugin = require('vue-loader/lib/plugin')
const path = require('path')

module.exports = {
  mode: 'development',
  // 1. 
  entry: {
    // __dirname: 최상위 위치(entry point); django 에서 BASE_DIR
    app: path.join(__dirname, 'src', 'main.js')
  },
  // 4. 
  module: {
    // 변환
    rules: [{
        test: /\.vue$/, // 정규 표현식; 확장자 .vue 인 것 모두를
        use: 'vue-loader', // 다음 플러그인을 사용하여 변환할 것임
      },
      {
        test: /\.css$/,
        use: ['vue-style-loader', 'css-loader'] // 여러 개는 배열로 작성
      }
    ]
  },
  // 3.
  plugins: [
    new VueLoaderPlugin(),
  ],
  // 2. 
  output: {
    filename: 'app.js',
    path: path.join(__dirname, 'dist'),
  },
}