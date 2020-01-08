<template>
  <div>
    <h1>여기는 최상위 컴포넌트(root component)입니다.</h1>
    <!-- 3. 사용 -->
    <todo-list category="취업 특강"></todo-list>
    <todo-list category="SSAFY"></todo-list>
    <todo-list category="기타"></todo-list>
  </div>
</template>

<script>
// 1. component 불러오기
import TodoList from "./components/TodoList.vue";

// 2. 불러온 component 를 최상위(부모) component 에 등록
export default {
  components: {
    TodoList
  }
};
</script>

<style>
</style>