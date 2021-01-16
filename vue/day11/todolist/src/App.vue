<template>
  <div id="app">
    <h1>Todo List</h1>
    <h2>전체 : {{allTodosCount}}</h2>
    <h3>완료 : {{completedTodosCount}}</h3>
    <h3>미완료 : {{uncompletedTodosCount}}</h3>
    <TodoForm />
    <TodoList />
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'


export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  computed: {
    ...mapGetters([
      'allTodosCount',
      'completedTodosCount',
      'uncompletedTodosCount',
    ])
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
