// Vue instance 를 최종으로 만드는 파일

// 1. 설치되어 있는 Vue 추가
// (직접 만든 파일이 아닌 경우(install 을 통해 생성된 경우),
// 현 위치에서 vue 이름을 가진 폴더가 존재하지 않음.
// 이때 자동으로 node_modules 에서 가져옴)
import Vue from 'vue'

// 2. 최상위 컴포넌트 추가
// (직접 작성한 파일) 상대 경로 표시
import App from './App.vue'



new Vue({
  render: h => h(App)
}).$mount('#app')