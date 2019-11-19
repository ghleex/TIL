<template>
  <div class="home">
    <h1>Todo w/ django</h1>
  </div>
</template>

<script>
// @ is an alias to /src
import router from '../router'

export default {
  name: 'home',
  components: {
    
  },
  methods: {
    checkLoggedIn() {
      this.$session.start()
      if (!this.$session.has('jwt')) {
        router.push('/login')
      }
    }
  },
  // DOM 에 Vue instance 가 mount 될 때마다 checkLoggedIn 이 실행되어 로그인 여부 체크
  mounted() {
    this.checkLoggedIn()
  },
}
</script>
