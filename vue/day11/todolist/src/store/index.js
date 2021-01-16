import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos:[
      {title:'할일1',completed:false},
      {title:'할일2',completed:true},
    ]
  },
  getters:{ 
    allTodosCount: function (state) {
      return state.todos.length
    },
    completedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === true
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.completed === false
      }).length
    },
  },
  mutations: {
    CREATE_TODO(state,todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO(state,todoItem) {
      const idx = state.todos.indexOf(todoItem)
      state.todos.splice(idx,1)
    },
    UPDATE_TODO_STATUS(state,todoItem) {
      state.todos = state.todos.map((todo)=> {
        if(todo===todoItem) {
          return {
            ...todo,
            completed: !todo.completed
          }
        }
        return todo
      })
    }
  },
  actions: {
    createTodo({commit},todoItem) {
      commit('CREATE_TODO',todoItem)
    },
    deleteTodo({commit},todoItem) {
      commit('DELETE_TODO',todoItem)
    },
    updateTodoStatus({commit},todoItem){
      commit('UPDATE_TODO_STATUS',todoItem)
    }
  },
  modules: {
  },
  plugins: [
    createPersistedState(),
  ]
})
