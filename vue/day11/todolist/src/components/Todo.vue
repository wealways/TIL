<template>
  <div>
    <span
      :class="{completed: todo.completed}"
      @click="updateTodoStatus"
    >
      {{todo.title}}
    </span>
    <button @click="deleteTodo">X</button>
  </div>
</template>

<script>
export default {
  name: 'Todo',
  props:{
    todo:Object,
  },
  methods: {
    updateTodoStatus() {
      this.$store.dispatch('updateTodoStatus',this.todo)
    },
    deleteTodo() {
      this.$store.dispatch('deleteTodo',this.todo)
    }
  }
}
</script>
<style>
  .completed{
    text-decoration: line-through;
  }
</style>