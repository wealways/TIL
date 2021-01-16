import Vue from 'vue'
import VueRouter from 'vue-router'

// 컴포넌트 등록하기
import TheLotto from '../views/TheLotto.vue'
// import Result from '../views/Result.vue'

Vue.use(VueRouter)

const routes = [
  
  {
    path: '/lotto/:lottoNum',
    name: 'TheLotto',
    component: TheLotto
  },
  // {
  //   path: '/result',
  //   name: 'Result',
  //   component: Result
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
