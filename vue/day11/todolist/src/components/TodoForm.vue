<template>
  <div>
    <label for="todoinput">할일: </label>
    <input 
      type="text" 
      id="todoinput"
      v-model.trim="todo"
      @keypress.enter="createTodo"
    >
    <button @click="createTodo">Add</button>
  </div>
</template>

<script>
export default {
  name:'TodoForm',
  data() {
    return {
      todo:'',
    }
  },
  methods: {
    createTodo() {
      const todoItem = {
        title: this.todo,
        completed: false,
      }
      if(todoItem && todoItem.title.trim())
        this.$store.dispatch('createTodo',todoItem)
      this.todo=''
    }
  }
  

}
</script>

<style>

</style>