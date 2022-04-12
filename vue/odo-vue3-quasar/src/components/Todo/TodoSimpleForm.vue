<template>
  <div class="flex">
    <q-form class="flex row content-center" @submit="onSubmit">
      <q-input
        outlined
        v-model="todo"
        style="min-width: 500px"
        placeholder="New todo"
      />
      <q-btn type="submit" label="Add"></q-btn>
    </q-form>
  </div>
  <div v-show="hasError" style="color: red">Cannot be empty</div>
</template>

<script>
import { ref } from "vue";
export default {
  emits: ["add-todo"],
  // context 중 emit만 사용하는 것.
  setup(props, { emit }) {
    const todo = ref("");
    const hasError = ref(false);
    const onSubmit = () => {
      if (todo.value === "") {
        hasError.value = true;
      } else {
        emit("add-todo", {
          id: Date.now(),
          subject: todo.value,
          completed: false,
        });
        hasError.value = false;
        todo.value = "";
      }
      return;
    };
    return {
      todo,
      hasError,
      onSubmit,
    };
  },
};
</script>

<style></style>
