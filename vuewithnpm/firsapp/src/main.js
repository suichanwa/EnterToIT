import Vue from 'vue/dist/vue.js';

var userData = {name:'tetsing', age:22}

var changeData = new Vue({
    el:'#app',
    data: userData
})

changeData.name = 'fuckSome';
changeData.age = 345;

new Vue({
  el: '#app',
  data: {
      message: 'fu!',
      name: 'tome',
      age: 23
  },
  methods: {
      setMessage: function(event){
          this.message = event.target.value;
      }
  }
})

new Vue({
    el:'#user_data',
    data:{
        counter: 0,
        name: 'first name',
        age: 34,
        template: '<p>Имя: {{name}}   Возраст {{age}}</p>',
        visible: true,
        users:[
            {name:'Tom', age:22},
            {name:'Bob', age:25},
            {name:'Sam', age:28},
            {name:'Alice', age:26}
        ],
        selectedUsers:[],
    },
    methods:{
        welcome: function(){
            return "naisu code";
        },
        displayName: function() {
            return this.name;
        },
        fac: function(n){
            var result = 1;
            for(var i = 1; i < n; i++){
                result = result * i;
            }  
            return result;
        },
        increse: function(n){
            this.counter = this.count + n;
        },
        decrese: function(n){
            this.counter = this.count - n;
        },
        change: function(){
            this.$refs.header.innerHTML = "testing";
            this.$refs.header.value;
        }
    }
});


new Vue({
    el:'#counter',
    data:{ cout:1 },
    methods:{
        inc: function(n,event){
            console.log(event);
            this.cout = this.cout + n;
        },
        dec: function(n, event){
            console.log(event.target);
            this.cout = this.cout - n;
        }
    }
})

new Vue({
    el:'#app2',
    data:{name: 'Tome', age:23},
    methods:{
        checkAge: function(){
            console.log("method");
            if(this.age > 17)
                return "доступ разрешен";
            else
                return "доступ запрещен";
        }
    }
})

new Vue({
    el:'#classes',
    data: {isActive : false}
})

new Vue({
    el:'#watch',
    data: {number: '', result: ''},
   
    watch:{
        number: function(newNumber){
            if(newNumber > 0);
                this.factorial(newNumber);
        }
    },
    methods:{
        factorial: function(newNumber){
            this.result = 'fac result...';
            var vm = this;
            setTimeout(function(){
                var res = 1;
                    for(var i = 1; i<=newNumber; i++){
                        res = res * i;
                    }
                    vm.result = 'factorial of number ' + newNumber + ' is ' + res;
            }, 2000);
        }
    }
})

Vue.component('some-thing',{
    template:'<h1>fucked </h1>'
})

new Vue({
    el:'#_app',
    data: {
        user :'name',
        message : 'somevalue'
    },
    methods:{
        chagne_name: function(){
            this.name = 'changed';
        }
    }
})

Vue.component('useredit-ed', {
    props: ["user"],
    data: function () {
      return { userName: this.user}
    },
    template: '<div><input type="text" v-model="userName" /><p>Name: {{userName}}</p></div>'
});

Vue.component('message-container',{
    props:'message that will be showed',
    template: '<h1>props testing</h1>'
})

Vue.filter('uppercase', function (value) {
    return value.toUpperCase();
  });