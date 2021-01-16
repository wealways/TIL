<template>
  <div>
    <Todo
      v-for="(todo,idx) in todos"
      :key="idx"
      :todo="todo"
    />
  </div>
</template>

<script>
import {mapState} from 'vuex'
import Todo from '@/components/Todo'
export default {
  name:'TodoList',
  components: {
    Todo
  },
  computed: {
    ...mapState([
      'todos',
    ])
  }
}
</script>

<style>

</style>