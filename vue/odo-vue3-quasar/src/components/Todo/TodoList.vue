<template>
  <div v-for="(todo, idx) in todos" :key="todo.id" class="q-ma-xs">
    <q-card
      class="my-card"
      @click="moveToPage(todo.id)"
      style="cursor: pointer"
    >
      <q-card-section class="flex justify-between">
        <q-checkbox
          v-model="todo.completed"
          @update:model-value="toggleTodo(idx)"
        >
          <template v-slot:default>
            <!-- <div :style="todo.completed ? todoStyle : {}"> -->
            <div :class="{ completed: todo.completed }">
              {{ todo.subject }}
            </div>
          </template>
        </q-checkbox>
        <q-btn @click.stop="deleteTodo(idx)" label="Delete" color="red"></q-btn>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
export default {
  props: {
    todos: {
      type: Array,
      required: true,
    },
  },
  // vue3
  emits: ["delete-todo", "toggle-todo"],
  setup(props, context) {
    const router = useRouter();
    const deleteTodo = (idx) => {
      context.emit("delete-todo", idx);
    };
    const toggleTodo = (idx) => {
      context.emit("toggle-todo", idx);
    };
    const moveToPage = (todoId) => {
      console.log(todoId);
      // router.push(`/todos/${todoId}`);
      router.push({
        name: "Todo",
        params: {
          id: todoId,
        },
      });
    };
    return { deleteTodo, toggleTodo, moveToPage };
  },
};
</script>

<style scoped>
.completed {
  text-decoration: line-through;
  color: gray;
}
</style>
