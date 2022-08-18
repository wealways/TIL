<template>
  <q-page class="flex column q-pa-md">
    <div>Todo</div>
    <q-input
      outlined
      v-model="searchKeyword"
      style="min-width: 500px"
      placeholder="Search"
      @keyup.enter="searchTodo"
    />
    <hr />
    <TodoSimpleForm @add-todo="addTodo" />
    <div style="color: red">{{ err }}</div>
    <div v-if="!todos.length">No data</div>
    <TodoList
      :todos="todos"
      @delete-todo="deleteTodo"
      @toggle-todo="toggleTodo"
    />
    <q-pagination
      v-model="paginationCurrent"
      color="purple"
      :max="numberOfPage"
      :max-pages="5"
      boundary-numbers
      boundary-links
    />
  </q-page>
</template>

<script>
import { defineComponent, ref, computed, watch } from "vue";
import TodoSimpleForm from "src/components/Todo/TodoSimpleForm.vue";
import TodoList from "src/components/Todo/TodoList.vue";
import { api } from "src/boot/axios";

export default defineComponent({
  name: "TodoIndex",
  components: {
    TodoSimpleForm,
    TodoList,
  },
  setup() {
    const todos = ref([]);
    const todosTotal = ref(0);
    const paginationCurrent = ref(1);
    const limit = 5;
    const numberOfPage = computed(() => {
      return Math.ceil(todosTotal.value / limit);
    });
    const err = ref("");
    const searchKeyword = ref("");

    // Get todo list
    const getTodos = async (page = paginationCurrent.value) => {
      err.value = "";
      try {
        const res = await api.get(
          `/todos?_page=${page}&_limit=${limit}&subject_like=${searchKeyword.value}&_sort=id&_order=desc`
        );
        todos.value = res.data;
        todosTotal.value = res.headers["x-total-count"];
      } catch (err) {
        err.value = "getTodos 에러";
      }
    };
    getTodos();
    // watchEffect 안에 reactive 가 있으면 내부 스코프 전체가 실행된다.
    // watchEffect, watch의 차이
    // watchEffect(() => {
    //   getTodos(paginationCurrent.value);
    // });
    watch(paginationCurrent, (now, prev) => {
      getTodos(paginationCurrent.value);
    });

    // Creat Todo
    const addTodo = async (todo) => {
      err.value = "";
      // boot file에 정의한  axios 를 가져와서 바로 사용.
      try {
        const res = await api.post("/todos", {
          subject: todo.subject,
          completed: todo.completed,
        });

        if (paginationCurrent.value !== 1) {
          paginationCurrent.value = 1;
        } else {
          getTodos(1);
        }
      } catch (err) {
        err.value = "addTodo 에러";
      }
    };

    //patch Todo
    const toggleTodo = async (idx) => {
      err.value = "";
      console.log(1);
      const id = todos.value[idx].id;
      console.log(2);
      try {
        const res = await api.patch(`/todos/${id}`, {
          completed: todos.value[idx].completed,
        });
        // todos.value[idx].completed = !todos.value[idx].completed;
      } catch (err) {
        err.value = "toggleTodo 에러";
      }
    };

    // Delete Todo
    const deleteTodo = async (idx) => {
      err.value = "";
      const id = todos.value[idx].id;
      try {
        await api.delete(`/todos/${id}`);
        // todos.value.splice(idx, 1);
        getTodos(paginationCurrent.value);
      } catch (err) {
        err.value = "deleteTodo 에러";
      }
    };

    // search
    let timeout = null;
    const searchTodo = () => {
      clearTimeout(timeout);
      getTodos(1);
    };
    watch(searchKeyword, (cur, prev) => {
      clearTimeout(timeout);
      timeout = setTimeout(() => {
        getTodos(1);
      }, 1000);
    });

    // // computed는 값을 캐시에 저장해놓는다. 그래서 값이 바뀌지 않으면, 재실행하지 않고 캐시에서 값을 가져온다.
    // const filteredTodos = computed(() => {
    //   if (searchKeyword.value) {
    //     return todos.value.filter((todo) => {
    //       return todo.subject.includes(searchKeyword.value);
    //     });
    //   }

    //   return todos.value;
    // });
    return {
      todos,
      numberOfPage,
      paginationCurrent,
      addTodo,
      toggleTodo,
      deleteTodo,
      searchKeyword,
      searchTodo,
      // filteredTodos,
      err,
    };
  },
});
</script>

<style scoped>
.completed {
  text-decoration: line-through;
  color: gray;
}
</style>
