<template>
   <div>
      <h3>Todos</h3>
      <div class=todos>
         <div v-for="todo in allTodos" :key="todo.id" class=todo>
            {{todo.title}}
         </div>
      </div>
   </div> 
</template>


<script>
import {mapGetters} from 'vuex';


export default {
   name: 'TodoS',
   computed: mapGetters(['allTodos'])
};



</script>

