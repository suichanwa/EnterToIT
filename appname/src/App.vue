<template>
  <div class="container">
      <Header title="testing"/>
      <Button text="add task" color="green"/>
  </div>

</template>

<script>
import Header from './components/Header.vue'
import Button from './components/Button.vue'

export default{
    name: 'App',
    components: {
      Header,
      Button
  },
}

</script>

