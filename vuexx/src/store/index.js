import Vuex from 'vuex';
import Vue from 'vue';
import TodoS from './modules/todos';


Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        TodoS 
    }
})