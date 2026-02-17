<template>
    <header>
        <h1> {{title}}</h1>
    </header>
</template>

<script>
    export default {
        name: 'Header',  
        props: {
            title: String,
            text:String,
            color:String,
        },
    }
</script>

<style scoped>
    Header {
        display: flex;
        justify-content: space-between;
        align-items:center;
        margin-bottom:20px;
    }

</style>
