<template>
  <div id="app">
    <div class="container">
      <TodoS /> 
    </div>
  </div>
</template>

<script>
import TodoS from './components/TodoS.vue';

export default {
  name: 'App',
  components: {
    TodoS
  }
}
</script>

<style>
body {
  line-height: 1.5;
  background: #fafafa;
}

.container{
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 20px;
}

</style>
