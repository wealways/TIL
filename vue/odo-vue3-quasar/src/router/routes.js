const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: "",
        name: "Home",
        component: () => import("src/pages/IndexPage.vue"),
      },
      {
        path: "/todos",
        name: "Todos",
        component: () => import("src/pages/TodoList/index.vue"),
      },
      {
        path: "/todos/:id",
        name: "Todo",
        component: () => import("src/pages/TodoList/_id.vue"),
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
