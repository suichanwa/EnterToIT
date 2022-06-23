const state = {
    todos: [
        {
            id: 1
            , title: 'Learn Vue'
            , completed: false
        },
        {
            id: 2
            , title: 'Learn Vuex'
            , completed: false
        }
    ]
};

const getter = {
    allTodos: state => state.todos
};

const actions = {};

const mutations = {};

export default {
    state,
    getter,
    actions,
    mutations
}