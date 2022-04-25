<template>
    <button @click="onClick()"  :style="{background:color }"
    class = "btn"> {{text}} </button>

</template>
    
<script>
export default {
    name: 'Button',
    props:{
        text:String,
        color: String,
    },
    methods:{
        onClick(){
            alert("testing");
        }
    },
    data(){
        return{
            tasks: [
                
            ]
        }
    }
}
</script>

<style scoped>

.btn {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

</style>
