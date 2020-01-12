<template>
  <div>    
    <LoginForm/>
  </div>
</template>

<script>
// @ is an alias to '/src'
  // import LoginForm from '../components/LoginForm'
  import LoginForm from '@/components/LoginForm'

  export default {
    name: 'login',
    components: {
      LoginForm,
    }
  }

</script>

<style>

</style>