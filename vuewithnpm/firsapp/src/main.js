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
      message: 'Hello Vue!',
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